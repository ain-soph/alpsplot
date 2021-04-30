#!/usr/bin/env python3

import argparse
import os

# https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6name.html
# https://onlinefontconverter.com/

# pip install fonttools


def split_ttc(filename: str):
    from fontTools.ttLib.ttCollection import TTCollection
    from fontTools.ttLib.ttFont import TTFont
    from fontTools.ttLib.tables._n_a_m_e import table__n_a_m_e, NameRecord
    ttc = TTCollection(file=filename)
    ttf_list: list[TTFont] = ttc.fonts
    dirname = os.path.dirname(filename)
    print(f'find {len(ttf_list):3d} font(s) in {filename}')
    for i, ttf in enumerate(ttf_list):
        font_name = ''
        name_table: table__n_a_m_e = ttf['name']
        try:
            record: NameRecord = name_table.names[6]
            if record.nameID == 6:
                font_name = record.toStr()
            else:
                raise IndexError()
        except IndexError:
            for record in name_table.names:
                if record.nameID == 6:
                    font_name = record.toStr()
        assert font_name != ''
        ttf_path = os.path.join(dirname, f'{font_name}.ttf')
        ttf.save(ttf_path)
        print(f'{i:3d}: {font_name:70} saved at {ttf_path}')


def split_ttc_old(filename: str):
    from struct import pack_into, unpack_from

    def ceil4(n: int) -> int:
        """returns the next integer which is a multiple of 4"""
        return (n + 3) & ~3

    newname = filename.removesuffix('.ttc').removesuffix('.TTC')
    with open(filename, 'rb') as in_file:
        buf = in_file.read()
    if buf[:4] != b"ttcf":
        with open(f'{newname}.ttf', 'wb') as out_file:
            out_file.write(buf)
    else:
        ttf_count = unpack_from("!L", buf, 0x08)[0]
        print("Contain TTF-files: %s" % ttf_count)
        ttf_offset_array = unpack_from("!" + ttf_count * "L", buf, 0x0C)
        for i in range(ttf_count):
            print("Extract TTF #%s:" % (i + 1))
            table_header_offset = ttf_offset_array[i]
            print("\tHeader offset Byte %s" % table_header_offset)
            table_count = unpack_from("!H", buf, table_header_offset + 0x04)[0]
            header_length = 0x0C + table_count * 0x10
            print("\tHeader length: %s Byte" % header_length)

            table_length = 0
            for j in range(table_count):
                length = unpack_from(
                    "!L", buf, table_header_offset + 0x0C + 0x0C + j * 0x10)[0]
                table_length += ceil4(length)

            total_length = header_length + table_length
            new_buf = bytearray(total_length)
            header = unpack_from(header_length * "c", buf, table_header_offset)
            pack_into(header_length * "c", new_buf, 0, *header)
            current_offset = header_length

            for j in range(table_count):
                pos = 0x14 + j * 0x10
                offset = unpack_from("!L", buf, table_header_offset + pos)[0]
                length = unpack_from("!L", buf, table_header_offset + pos+4)[0]
                pack_into("!L", new_buf, pos, current_offset)
                current_table = unpack_from(length * "c", buf, offset)
                pack_into(length*"c", new_buf, current_offset, *current_table)
                # table_checksum = sum(unpack_from("!"+("L"*length), new_buf, current_offset))
                # pack_into("!L", new_buf, 0x0C+0x04+j*0x10, table_checksum)
                current_offset += ceil4(length)
            with open(f'{newname}{i:d}.ttf', 'wb') as out_file:
                out_file.write(new_buf)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename: str = args.filename
    split_ttc(filename)


if __name__ == '__main__':
    main()

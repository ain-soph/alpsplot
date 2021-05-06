#!/usr/bin/env python3

import numpy as np
import scipy.stats as stats


def get_roc_curve(label: np.ndarray, pred: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    total_inst = len(label)
    total_pos_inst = len(np.where(label == 1)[0])

    assert len(label) == len(pred)
    # true positive rates and false positive rates
    tprs, fprs, thresholds = [], [], []

    # iterate over all positive thresholds
    for threshold in np.unique(pred):
        pred_pos_idx: np.ndarray = np.where(pred >= threshold)[0]
        # number of predicted positive instances
        pred_pos_inst = len(pred_pos_idx)
        # number of true positive instances
        true_pos_inst: int = np.count_nonzero(label[pred_pos_idx])

        tpr = true_pos_inst / total_pos_inst
        fpr = (pred_pos_inst - true_pos_inst) / (total_inst - total_pos_inst)
        tprs.append(tpr)
        fprs.append(fpr)
        thresholds.append(threshold)
    return np.array(fprs), np.array(tprs)


def normalize(x: np.ndarray, _min: float = None, _max: float = None, tgt_min: float = 0.0, tgt_max: float = 1.0) -> np.ndarray:
    _min = float(x.min()) if _min is None else _min
    _max = float(x.max()) if _max is None else _max
    x = (x - _min) / (_max - _min) * (tgt_max - tgt_min) + tgt_min
    return x


def avg_smooth(x: np.ndarray, window: int = 3) -> np.ndarray:
    new_x = np.zeros_like(x)
    for i in range(len(x)):
        if i < window // 2:
            new_x[i] = (x[0] * (window // 2 - i) +
                        np.sum(x[: i + (window + 1) // 2])) / window
        elif i >= len(x) - (window - 1) // 2:
            new_x[i] = (x[-1] * ((window + 1) // 2 - len(x) + i) +
                        np.sum(x[i - window // 2:])) / window
        else:
            new_x[i] = np.mean(x[i - window // 2: i + 1 + (window - 1) // 2])
    return new_x


def monotone(x: np.ndarray, increase: bool = True) -> np.ndarray:
    y = np.copy(x)
    temp: float = min(x) if increase else max(x)
    for i in range(len(x)):
        if ((increase and x[i] < temp) or (not increase and x[i] > temp)):
            y[i] = temp
        else:
            temp = x[i]
    return y


def gaussian_kde(x: np.ndarray, x_grid: np.ndarray) -> np.ndarray:
    kde_func = stats.gaussian_kde(x)
    y_grid = kde_func(x_grid)
    return y_grid


def groups_err_bar(x: np.ndarray, y: np.ndarray) -> dict[float, np.ndarray]:
    y_dict = {}
    for _x in set(x):
        y_dict[_x] = np.array([y[t] for t in range(len(y)) if x[t] == _x])
    return y_dict


def flatten_err_bar(y_dict: dict[float, np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    x = []
    y = []
    for _x in y_dict.keys():
        for _y in y_dict[_x]:
            x.append(_x)
            y.append(_y)
    return np.array(x), np.array(y)


def adjust_err_bar(y_dict: dict[float, np.ndarray], mean: np.ndarray = None, std: np.ndarray = None) -> dict[float, np.ndarray]:
    sort_keys = np.sort(list(y_dict.keys()))
    if isinstance(mean, float):
        mean = mean * np.ones(len(sort_keys))
    if isinstance(std, float):
        std = std * np.ones(len(sort_keys))
    for i in range(len(sort_keys)):
        key = sort_keys[i]
        if mean is not None and mean[i]:
            y_dict[key] = y_dict[key] + mean[i]
        if std is not None and std[i]:
            y_dict[key] = y_dict[key].mean() \
                + (y_dict[key] - y_dict[key].mean()) * std[i]
    return y_dict


def normalize_err_bar(x: np.ndarray, y: np.ndarray):
    x = normalize(x)
    y_dict = groups_err_bar(x, y)
    y_mean = np.array([y_dict[_x].mean()
                       for _x in np.sort(list(y_dict.keys()))])
    y_norm = normalize(y_mean)
    y_dict = adjust_err_bar(y_dict, y_norm - y_mean)
    return flatten_err_bar(y_dict)


def avg_smooth_err_bar(x: np.ndarray, y: np.ndarray, window: int = 3):
    y_dict = groups_err_bar(x, y)
    y_mean = np.array([y_dict[_x].mean()
                       for _x in np.sort(list(y_dict.keys()))])
    y_smooth = avg_smooth(y_mean, window=window)
    y_dict = adjust_err_bar(y_dict, y_smooth - y_mean)
    return flatten_err_bar(y_dict)

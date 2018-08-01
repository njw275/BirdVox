from joblib import Parallel, delayed
import numpy as np

import countingOnsets as co
import DetectionEvalSourceCode as det
import GetF as gf
import HPC_Paths as p
import Split as sp
import startTimes as st

#for split_id:
test_fmeasures = []
fmin_input = 1500
h_length = 256
sr = 22050
h_duration = h_length / sr
start_time = 0
steps = 0
thresholds = []
threshold = 0.0
max_threshold = 1.51
while (threshold<max_threshold):
    thresholds.append(threshold)
    threshold += 0.01
units = [1, 2, 3, 5, 7, 10]
epsilon = np.finfo(float).eps

for split_id in range(len(units)):
    test_set, training_set = sp.split_units(split_id)
    #training_set.pop(training_set.index(10))
    print("Testing on unit " + str(test_set[0]).zfill(2))

    threshold_Fs = Parallel(n_jobs=-1)(delayed(gf.get_F)(training_set, th) for th in thresholds)

    # find best threshold (argmax) and print it to slurm
    best_threshold_id = np.argmax(threshold_Fs)
    best_threshold = thresholds[best_threshold_id]
    best_threshold_str = "{0:.2f}".format(best_threshold)
    best_F = np.max(threshold_Fs)
    best_F_str = "{0:.2f}".format(100*best_F)
    print("Best F measure for training: " + best_F_str + "%")
    print("Best threshold for training: " + best_threshold_str)

    test_num_onsets = 0
    test_true_pos = 0
    test_false_neg = 0
    test_false_pos = 0
    test_precision = []
    test_recall = []
    test_fmeasure = []

    for unit in test_set:
        Tp, Fp, Fn = det.threshold(unit, start_time, best_threshold)

        test_num_onsets += co.counting_onsets(unit,start_time)
        test_true_pos += Tp
        test_false_neg += Fn
        test_false_pos += Fp

    if (test_true_pos + test_false_pos) == 0:
        test_P = 0
    else:
        test_P = test_true_pos / (test_true_pos + test_false_pos)

    if (test_true_pos + test_false_neg) == 0:
        test_R = 0
    else:
        test_R = test_true_pos / (test_true_pos + test_false_neg)

    if test_P<epsilon and test_R<epsilon:
        test_F = 0.0
    else:
        test_F = 2*test_P*test_R / (test_P + test_R)
    test_fmeasures.append(test_F)

# print average and std of Ftest across chunks (this is the final metric)
print("")
print("Test F Measures")
for fmeasures in test_fmeasures:
    print(fmeasures)
print("")
avg_test_F = np.average(test_fmeasures)
avg_test_F_str = "{0:.2f}".format(100*avg_test_F)
std_test_F = np.average(test_fmeasures)
std_test_F_str = "{0:.2f}".format(100*std_test_F)
print("")
print("F test: " + avg_test_F_str + "% +/- " + std_test_F_str)


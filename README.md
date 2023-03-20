You need to use the `csv` files in the same folder to test the code. The `csv` files in the `machine_learning`folder and `preferentialAttachment` folder are not the original data we get from the twitter, they are the edge processed by `read_edge.py`. If you want to test `read_edge.py`, you can just use the two `csv` files, they are the original edge file we get. `read_edge.py` will generate `new_edge.csv` and `node.csv`. `new_edge.csv` is the new edge file and `node.csv` is the new node file. These two files are correct files used in the `machine_learning.py`. In `preferentialAttachment.py`, we only need `new_edge.csv`. However, `Source` and `Target` should be added in the first line in order to run successfully. I have already added in the two edge files in `preferentialAttachment` folder for you, so that you don’t need to change it.
Please note that the result of `machine_learning.py` changes from time to time but are just tiny differences. So that the result you get may differ from the result in the report, but only a little.

The `preferentialAttachment.py` output like this:

```python
Please input the edge file name: lol_edge.csv
How many iterations?
10
Edges:
Iteration: 0: New edge: 6 - 32	(score:7906) is added!
Iteration: 1: New edge: 6 - 53	(score:5805) is added!
Iteration: 2: New edge: 6 - 66	(score:4488) is added!
Iteration: 3: New edge: 6 - 191	(score:4110) is added!
Iteration: 4: New edge: 6 - 149	(score:4002) is added!
Iteration: 5: New edge: 3 - 6	(score:3753) is added!
Iteration: 6: New edge: 6 - 133	(score:3640) is added!
Iteration: 7: New edge: 6 - 47	(score:3666) is added!
Iteration: 8: New edge: 6 - 514	(score:3550) is added!
Iteration: 9: New edge: 32 - 64	(score:3360) is added!
are added to the graph successfully!

进程已结束,退出代码0
```

The `machine_learning.py` output like this:

```python
Please input node file: cs_node.csv
Please input edge file: cs_edge.csv
Please wait a second!
E:\22FA\ECE4440J\project\code\predict\main.py:80: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  data = data.append(target[['node_1', 'node_2', 'link']], ignore_index=True)
Computing transition probabilities: 100%|██████████| 594/594 [00:00<00:00, 11911.25it/s]
Generating walks (CPU: 1): 100%|██████████| 50/50 [00:01<00:00, 39.10it/s]
E:\22FA\ECE4440J\project\code\predict\venv\lib\site-packages\lightgbm\engine.py:181: UserWarning: 'early_stopping_rounds' argument is deprecated and will be removed in a future release of LightGBM. Pass 'early_stopping()' callback via 'callbacks' argument instead.
  _log_warning("'early_stopping_rounds' argument is deprecated and will be removed in a future release of LightGBM. "
[LightGBM] [Info] Number of positive: 15, number of negative: 4331
[LightGBM] [Warning] Auto-choosing col-wise multi-threading, the overhead of testing was 0.003377 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 25500
[LightGBM] [Info] Number of data points in the train set: 4346, number of used features: 100
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.003451 -> initscore=-5.665504
[LightGBM] [Info] Start training from score -5.665504
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[1]	valid_0's auc: 0.771351
Training until validation scores don't improve for 20 rounds
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[2]	valid_0's auc: 0.409296
[3]	valid_0's auc: 0.785731
[4]	valid_0's auc: 0.752665
[5]	valid_0's auc: 0.750234
[6]	valid_0's auc: 0.754862
[7]	valid_0's auc: 0.761364
[8]	valid_0's auc: 0.411815
[9]	valid_0's auc: 0.668551
[10]	valid_0's auc: 0.792028
[11]	valid_0's auc: 0.797505
[12]	valid_0's auc: 0.705395
[13]	valid_0's auc: 0.808985
[14]	valid_0's auc: 0.809571
[15]	valid_0's auc: 0.818709
[16]	valid_0's auc: 0.818123
[17]	valid_0's auc: 0.805471
[18]	valid_0's auc: 0.811621
[19]	valid_0's auc: 0.70519
[20]	valid_0's auc: 0.802659
[21]	valid_0's auc: 0.804417
[22]	valid_0's auc: 0.803187
[23]	valid_0's auc: 0.803889
[24]	valid_0's auc: 0.801254
[25]	valid_0's auc: 0.805647
[26]	valid_0's auc: 0.807463
[27]	valid_0's auc: 0.810626
[28]	valid_0's auc: 0.790886
[29]	valid_0's auc: 0.803128
[30]	valid_0's auc: 0.830248
[31]	valid_0's auc: 0.7862
[32]	valid_0's auc: 0.819178
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[33]	valid_0's auc: 0.875586
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[34]	valid_0's auc: 0.903643
[35]	valid_0's auc: 0.905108
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[36]	valid_0's auc: 0.899075
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[37]	valid_0's auc: 0.907451
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[38]	valid_0's auc: 0.904405
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[39]	valid_0's auc: 0.912664
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[40]	valid_0's auc: 0.912664
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[41]	valid_0's auc: 0.912664
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[42]	valid_0's auc: 0.912664
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[43]	valid_0's auc: 0.912664
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[44]	valid_0's auc: 0.895209
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[45]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[46]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[47]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[48]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[49]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[50]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[51]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[52]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[53]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[54]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[55]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[56]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[57]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[58]	valid_0's auc: 0.89515
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
[59]	valid_0's auc: 0.89515
Early stopping, best iteration is:
[39]	valid_0's auc: 0.912664

```


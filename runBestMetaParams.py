from clusteringGPUMinutes import visualize_clusters

def main():
    run_params = [
        {"washout_period": 60, "activity_bin_before_pain_survey": 30, "activity_bin_after_pain_survey": 0,
         "sleep_binning_direction": "backward"},
        {"washout_period": 60, "activity_bin_before_pain_survey": 0, "activity_bin_after_pain_survey": 30,
         "sleep_binning_direction": "backward"},
        {"washout_period": 60, "activity_bin_before_pain_survey": 30, "activity_bin_after_pain_survey": 30,
         "sleep_binning_direction": "backward"},
        {"washout_period": 60, "activity_bin_before_pain_survey": 30, "activity_bin_after_pain_survey": 0,
         "sleep_binning_direction": "forward"},
        {"washout_period": 60, "activity_bin_before_pain_survey": 0, "activity_bin_after_pain_survey": 30,
         "sleep_binning_direction": "forward"},
        {"washout_period": 60, "activity_bin_before_pain_survey": 30, "activity_bin_after_pain_survey": 30,
         "sleep_binning_direction": "forward"},
        {"washout_period": 120, "activity_bin_before_pain_survey": 60, "activity_bin_after_pain_survey": 0,
         "sleep_binning_direction": "backward"},
        {"washout_period": 120, "activity_bin_before_pain_survey": 0, "activity_bin_after_pain_survey": 60,
         "sleep_binning_direction": "backward"},
        {"washout_period": 120, "activity_bin_before_pain_survey": 60, "activity_bin_after_pain_survey": 60,
         "sleep_binning_direction": "backward"},
        {"washout_period": 120, "activity_bin_before_pain_survey": 60, "activity_bin_after_pain_survey": 0,
         "sleep_binning_direction": "forward"},
        {"washout_period": 120, "activity_bin_before_pain_survey": 0, "activity_bin_after_pain_survey": 60,
         "sleep_binning_direction": "forward"},
        {"washout_period": 120, "activity_bin_before_pain_survey": 60, "activity_bin_after_pain_survey": 60,
         "sleep_binning_direction": "forward"}
    ]

    results = {"RCS02": [{'best_params': {'min_cluster_size': 50, 'min_samples': 6, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.7538812400859979}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.6349127330269431}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.6691871683264445}, {'best_params': {'min_cluster_size': 50, 'min_samples': 9, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.5951041532227545}, {'best_params': {'min_cluster_size': 50, 'min_samples': 7, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.3854091574794224}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.7819033050544237}, {'best_params': {'min_cluster_size': 50, 'min_samples': 6, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'leaf', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.3917685306276604}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.6953726517875921}, {'best_params': {'min_cluster_size': 50, 'min_samples': 6, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'leaf', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.472015042642382}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 1, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.3772423803733719}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.28029219249851056}, {'best_params': {'min_cluster_size': 50, 'min_samples': 5, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.4585570444961356}],
               "RCS04": [{'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.7333837857019261}, {'best_params': {'min_cluster_size': 50, 'min_samples': 6, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.6754934459731017}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 1, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.521335919528029}, {'best_params': {'min_cluster_size': 52, 'min_samples': 4, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.7232407018108786}, {'best_params': {'min_cluster_size': 50, 'min_samples': 9, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'leaf', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': 0.2654706336960227}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'leaf', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': 0.06308222456369846}, {'best_params': {'min_cluster_size': 50, 'min_samples': 9, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.21916458950772655}, {'best_params': {'min_cluster_size': 50, 'min_samples': 8, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.07468417424615803}, {'best_params': {'min_cluster_size': 50, 'min_samples': 2, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.4724516612164029}, {'best_params': {'min_cluster_size': 50, 'min_samples': 8, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.726242684929547}, {'best_params': {'min_cluster_size': 54, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.24363430280142104}, {'best_params': {'min_cluster_size': 50, 'min_samples': 8, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.5750018091427502}],
               "RCS06": [{'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.3848665379980007}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 1, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.08213688391441436}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.6840857223928556}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'sqeuclidean', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': 0.43571804162394523}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.43733250362209564}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.2146366449918203}, {'best_params': {'min_cluster_size': 50, 'min_samples': 7, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.11025304749355844}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.4231248788449624}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.31654166251095983}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': -0.3668553563020711}, {'best_params': {'min_cluster_size': 50, 'min_samples': 1, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': 0.014645437546523893}, {'best_params': {'min_cluster_size': 50, 'min_samples': 5, 'cluster_selection_epsilon': 0, 'metric': 'correlation', 'cluster_selection_method': 'eom', 'alpha': 1.0, 'allow_single_cluster': False, 'gen_min_span_tree': True}, 'vi': 0.3950752379865991}]}

    n_jobs = -1
    gen_imgs = True
    hyperparam_tune = False

    for pt_id, result_params in results.items():
        # Finding the best result based on 'vi'
        best_index, best_result = max(enumerate(result_params), key=lambda x: x[1]['vi'])

        # Accessing corresponding meta parameters from run_params
        best_meta_params = run_params[best_index]

        # Accessing the best HDBSCAN parameters
        best_hdbscan_params = best_result['best_params']

        # Printing the best results
        print(f"Patient ID: {pt_id}")
        print(f"Best Meta Parameters: {best_meta_params}")
        print(f"Best HDBSCAN Parameters: {best_hdbscan_params}")
        print(f"Best VI: {best_result['vi']}")
        print(f"Index of Best VI: {best_index}")

        best_params, vi = visualize_clusters(pt_id,
                                             best_meta_params["washout_period"],
                                             best_meta_params["activity_bin_before_pain_survey"],
                                             best_meta_params["activity_bin_after_pain_survey"],
                                             best_meta_params["sleep_binning_direction"],
                                             n_jobs,
                                             gen_imgs,
                                             hyperparam_tune,
                                             best_hdbscan_params)

        print(f"Confirmation from HDBSCAN run - Best HDBSCAN Parameters: {best_params}")
        print(f"Confirmation from HDBSCAN run - Best VI: {vi}")

if __name__ == "__main__":
    main()
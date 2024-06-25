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

    pt_ids = ["RCS02", "RCS04", "RCS06"]
    n_jobs = -1
    gen_imgs = False

    for pt_id in pt_ids:
        results = []

        for params in run_params:
            # Print the arguments
            print(f"Patient IDs: ", pt_id)
            print(f"Washout Period: ", params["washout_period"])
            print(f"Activity bin before pain survey: ", params["activity_bin_before_pain_survey"])
            print(f"Activity bin after pain survey: ", params["activity_bin_after_pain_survey"])
            print(f"Sleep binning direction: ", params["sleep_binning_direction"])
            print(f"Number of jobs: ", n_jobs)
            best_params, vi = visualize_clusters(pt_id,
                               params["washout_period"],
                               params["activity_bin_before_pain_survey"],
                               params["activity_bin_after_pain_survey"],
                               params["sleep_binning_direction"],
                               n_jobs,
                               gen_imgs)
            result = {"best_params": best_params, "vi": vi}
            results.append(result)

        print("Meta Grid Search Results")
        print("Patient id: ", pt_id)
        print("Results: ", results)
        print("Overall best params: ", max(results, key=lambda x: x["vi"])["best_params"])
        print("Overall best validity index: ", max(results, key=lambda x: x["vi"])["vi"])

if __name__ == "__main__":
    main()
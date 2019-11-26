import sys
import score_manager as scmanager



def extract_params():
    PARAM_COUNT = 7
    feature_data_file_path = None
    feature_labels_file_path = None
    output_path = None

    n_features = None

    if len(sys.argv) >= PARAM_COUNT:
        for i in range(1, len(sys.argv), 2):
            if sys.argv[i] == "-i" or sys.argv[i] == "--input":
                i = i + 1
                feature_data_file_path = sys.argv[i]
            if sys.argv[i] == "-l" or sys.argv[i] == "--label":
                i = i + 1
                feature_labels_file_path = sys.argv[i]
            if sys.argv[i] == "-n" or sys.argv[i] == "--n-features":
                i = i + 1
                n_features = int(sys.argv[i])

    return feature_data_file_path, feature_labels_file_path, n_features






def main():
    feature_data_file_path, feature_labels_file_path, n_features = extract_params()    



    if feature_data_file_path == None or feature_labels_file_path == None or n_features == None:
        print("Incorret parameters.\nType -h or --help for help.")
    
    else :
        feature_labels = scmanager.load_labels(feature_labels_file_path)
        feature_data = scmanager.load_data(feature_data_file_path)
        score_data, score_labels = scmanager.calc_scores(feature_data)

        result_dict = scmanager.generate_dict(feature_labels, score_labels, score_data)

        print(result_dict)


if __name__ == "__main__":
    main()
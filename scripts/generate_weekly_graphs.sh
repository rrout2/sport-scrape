while getopts i:o: flag
do
    case "${flag}" in
        i) input_path=${OPTARG};;
        o) output_path=${OPTARG};;
    esac
done

python src/visualizations/generate_weekly_graphs.py -i $input_path -o $output_path

while getopts i: flag
do
    case "${flag}" in
        i) input_path=${OPTARG};;
    esac
done

python src/generate_week.py -i $input_path
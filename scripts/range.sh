while getopts s:e:l:n: flag
do
    case "${flag}" in
        s) start_week=${OPTARG};;
        e) end_week=${OPTARG};;
        l) league_id=${OPTARG};;
        n) name=${OPTARG};;
    esac
done

python src/weekly_scrape.py -l $league_id -s $start_week -e $end_week -n $name

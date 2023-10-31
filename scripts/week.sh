while getopts w:l:n: flag
do
    case "${flag}" in
        w) week_number=${OPTARG};;
        l) league_id=${OPTARG};;
        n) name=${OPTARG};;
    esac
done

python src/scrape/weekly_scrape.py -l $league_id -s $week_number -e $week_number -n $name

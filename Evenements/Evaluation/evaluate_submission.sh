combine_py="/Users/nadi/workspace/HackaTAL2016/Evenements/Evaluation/combine_event_files.py"
eval_py="/Users/nadi/workspace/HackaTAL2016/Evenements/Evaluation/eval_events_euro2016.py"

if [ "$#" -ne 3 ]; then
   echo "Illegal number of parameters $#"
   exit 1
fi

tmp=`realpath $1`
gold_tsv=`realpath $2`
submission=`realpath $3`

archive=${submission##*/}
base=${archive%%.*}
team=${base%_*}
system=${base#*_}
         
mkdir -p $tmp
cd $tmp
tar -zxf $submission
python $combine_py *.tsv > pred.tsv
python $eval_py -s $system -t $team $gold_tsv pred.tsv
rm -rf $tmp
scriptname=$1

if [ $# -eq 0 ]
  then
    echo "No arg supplied"
    exit 1
fi

allpids=$(pgrep -f $scriptname)

echo "Processes found: " $allpids

 for cid in $allpids; do
    if [ "$cid" != "$$" ]
     then
      echo "killing process... " $cid
      killed=$(kill -9 $cid)
     else
      echo "Skipping pid: "+ $cid
    fi

 done

#echo "Founds pics": $allpids


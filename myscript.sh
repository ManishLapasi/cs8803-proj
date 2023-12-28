curr_time=$(date +"%Y-%m-%d_%H-%M-%S")
time_to_rec=5
input_file="num_runs.txt"
num_runs=10
if [ -e "$input_file" ]; then
  while IFS= read -r line; do
    number=$((line+1))
    echo "run number: $number"
    mkdir "test_dir_gd_$number"
    i=1
    while [ "$i" -le "$num_runs" ]; do
      /usr/bin/arecord -d $time_to_rec --format=S32_LE -r 44100 -t wav "/home/cs8803mci-team/test_dir_gd_$number/test_$curr_time-$number-$i.wav" > "log.txt" 2>"err.txt"
      i=$((i+1))
    done
    echo "$number" > "$input_file"
    sudo cp -r "/home/cs8803mci-team/test_dir_gd_$number" "/boot"
  done < "$input_file"
else
  echo "$input_file not found"
fi

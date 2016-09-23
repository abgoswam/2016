echo "Hello World"

# array=( one two three )

lambda=( 0.5 1 )
initial_t=( 0 0.5 )
decay_rate=( 0.75 1 )
power_t=( 0 0.5 )

for ld in "${lambda[@]}"
do
  for it in "${initial_t[@]}"
  do	
	for de in "${decay_rate[@]}"
	do
		for po in "${power_t[@]}"
		do	
			echo "MWT with CTR (lambda:" $ld,"initial_t:" $it, "decay_learningrate :" $de, "power_t:" $po")"
			vw --cb_explore_adf --rank_all -d ydata-fp-td-clicks-v1_0.20090502.vwprime -l ${ld} --initial_t ${it} --decay_learning_rate ${de} --power_t ${po} -p data.score_vwprime_lambda${ld}_initialt${it}_decay${de}_power${po}
			python evaluator_ips.py ydata-fp-td-clicks-v1_0.20090502.obs data.score_vwprime_lambda${ld}_initialt${it}_decay${de}_power${po}
		done
	done
  done
done
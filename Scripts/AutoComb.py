import os
from subprocess import call
import json
import re
import threading
#from tqdm import tqdm

dir_home = '/home/011/c/cr/crz180000/CS6304/Project2'
dir_gem5 = f'{dir_home}/gem5'
dir_spec = f'{dir_home}/Project1_SPEC'
dir_output = f'{dir_home}/ProjectTwo-Cache/Results'

benchmarks = [('401.bzip2', 'input.program 10'), ('429.mcf', 'inp.in')]

# L2 SIZE JUST SAYS MB SO 1-512?
configs = {
	'l1d_size': [
		'1kB', '2kB', '4kB', '8kB', '16kB', '32kB', '64kB', '128kB'
	],
	'l1d_assoc': [
		'1', '2', '4', '8'
	],
	'l1i_size': [
		'1kB', '2kB', '4kB', '8kB', '16kB', '32kB', '64kB', '128kB'
	],
	'l1i_assoc': [
		'1', '2', '4', '8'
	],
	'l2_size': [
		'256kB', '512kB', '1MB'
	],
	'l2_assoc': [
		'1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192', '16384'
	],
	'cacheline_size': [
		'8', '16', '32', '64', '128', '256', '512'
	]
}

def keysFromInd(ind):
	keylist = list(configs.keys())
	return {keylist[i]: configs[keylist[i]][ind[i]] for i in range(0,len(keylist))}

def paramsFromKeys(keys):
	return ' '.join([f'--{k}={keys[k]}' for k in keys])

def componentize(base, samp):
	ret = []
	for i in range(0, len(samp)):
		t = [samp[j] if i == j else base[j] for j in range(0,len(base))]
		if t not in ret:
			ret.append(t)
	return ret

def runGem5Sim(benchmark, benchmark_params, params, output):
	#Not plug and play for additional benchmarks but works for 401 and 429
	call(f'time {dir_gem5}/build/X86/gem5.opt -d {dir_output}/{output} {dir_gem5}/configs/example/se.py -I 500000000 -c {dir_spec}/{benchmark}/src/benchmark -o \"{dir_spec}/{benchmark}/data/{benchmark_params}\" --cpu-type=timing --caches --l2cache {params}', shell=True)

def runBenchmark(benchmark, params, output):
	call(f'rm -rf {dir_output}/{output}/*', shell=True)
	runGem5Sim(benchmark[0], benchmark[1], params, output)
	print(f'Finished benchmark {benchmark[0]} with {params}')

#call(f'{dir_gem5}/build/X86/gem5.opt -d {dir_output}/TEMP {dir_gem5}/configs/example/se.py -I 500000000 -c {dir_spec}/401.bzip/src/benchmark -o {dir_spec}/401.bzip/data/input.program --cpu-type=timing --caches --l2cache {paramsFromKeys(keysFromInd([0,0,0,0,0,0,0]))}', shell=True)
#call(f'{dir_spec}/401.bzip/run.sh')
# Low, Medium, High as specified
# Low
# Medium
# High
# Old baselines
#param_grid_t = [[0, 0, 0, 0, 0, 0, 0], [6, 2, 6, 2, 1, 12, 3], [7, 3, 7, 3, 2, 13, 4]]
# New baseline
baseline_grid = [[7, 1, 7, 1, 2, 0, 3]]
modification_grid = [[7, 3, 7, 3, 2, 14, 6], [0, 0, 0, 0, 0, 0, 0]]
param_grid_t = baseline_grid + [v for k in [componentize(i, j) for i in baseline_grid for j in modification_grid] for v in k]
param_grid = []
[param_grid.append(v) for v in param_grid_t if v not in param_grid]
os.chdir(dir_gem5)
print(f'Params to run: {param_grid}')
threads = []
for p in param_grid:
	print(f'Running permutation: {p}')
	for bm in benchmarks:
		params = paramsFromKeys(keysFromInd(p))
		perm_str = f'Perm_{"_".join([str(i) for i in p])}_{bm[0]}'
		t = threading.Thread(target=runBenchmark, args=(bm, params, perm_str,))
		threads.append(t)
		t.start()
		#runBenchmark(bm, params, perm_str)
		# Remove previous run
		"""
		call(f'rm -rf {dir_output}/{perm_str}/*', shell=True)
		# Call for 429 benchmark
		if bm == '429':
			call(f'{dir_gem5}/build/X86/gem5.opt -d {dir_output}/{perm_str} {dir_gem5}/configs/example/se.py -I 500000000 -c {dir_spec}/429.mcf/src/benchmark -o {dir_spec}/429.mcf/data/inp.in --cpu-type=timing --caches --l2cache {paramsFromKeys(k)}', shell=True)
		elif bm == '401':
			call(f'{dir_gem5}/build/X86/gem5.opt -d {dir_output}/{perm_str} {dir_gem5}/configs/example/se.py -I 500000000 -c {dir_spec}/401.bzip2/src/benchmark -o \"{dir_spec}/401.bzip2/data/input.program 10\" --cpu-type=timing --caches --l2cache {paramsFromKeys(k)}', shell=True)
			#call(f'{dir_spec}/401.bzip/run.sh')
			#time /home/010/c/cr/crz180000/CS6304/Project2/gem5/build/X86/gem5.opt -d ../ProjectTwo-Cache/Results/m5out /home/010/c/cr/crz180000/CS6304/Project2/gem5/configs/example/se.py -c ../Project1_SPEC/401.bzip2/src/benchmark -o "../Project1_SPEC/401.bzip2/data/input.program 10" -I 500000000 --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64
		else:
			print('Unknown benchmark')
		"""
		# Call for hello world
		#call(f'{dir_gem5}/build/X86/gem5.opt -d {dir_output}/TEMP {dir_gem5}/configs/example/se.py -I 500000000 -c {dir_gem5}/tests/test-progs/hello/bin/x86/linux/hello --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64', shell=True)

		# Copy simulated data to run unique folder
		#call(f'mkdir {dir_output}/{perm_str}', shell=True)
		#call(f'mv -f {dir_output}/TEMP/* {dir_output}/{perm_str}/', shell=True)

		#resFile = open(f'{dir_output}/TEMP/stats.txt', 'r')
		#regex_row = re.compile('([^ \t\n]+)[ \n\t]+([^ \t\n]+)[ \n\t]+([^ \t\n]+)')
		#d = {'' if r is None else r.group(1): '' if r is None else r.group(2) for r in [regex_row.match(l) for l in resFile.read().splitlines()]}
		#print(f'Instr cache miss: {d["system.cpu.icache.overall_miss_rate::total"]}, Data cache miss: {d["system.cpu.dcache.overall_miss_rate::total"]}, L2 Miss rate: {d["system.l2.overall_miss_rate::total"]}')

for t in threads:
	t.join()
print('All threads complete')
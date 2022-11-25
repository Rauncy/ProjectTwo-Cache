import os
from subprocess import call
import json
import re
#from tqdm import tqdm

dir_home = '/home/011/c/cr/crz180000/CS6304/Project2'
dir_gem5 = f'{dir_home}/gem5'
dir_spec = f'{dir_home}/Project1_SPEC'
dir_output = f'{dir_home}/Results'

os.chdir(dir_gem5)

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
		'256kB', '512kB', '1MB', '2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB', '512MB'
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

def componentize(arr):
	ret = []
	for i in range(0, len(arr)):
		t = [0,0,0,0,0,0,0]
		t[i] = arr[i]
		ret.append(t)
	return ret

#call(f'{dir_gem5}/build/X86/gem5.opt -d {dir_output}/TEMP {dir_gem5}/configs/example/se.py -I 500000000 -c {dir_spec}/401.bzip/src/benchmark -o {dir_spec}/401.bzip/data/input.program --cpu-type=timing --caches --l2cache {paramsFromKeys(keysFromInd([0,0,0,0,0,0,0]))}', shell=True)
#call(f'{dir_spec}/401.bzip/run.sh')
#Low, Medium, High as specified in discord
param_grid = [[0, 0, 0, 0, 0, 0, 0], [4, 2, 4, 2, 1, 13, 5], [5, 3, 5, 3, 2, 14, 6]]
param_grid = param_grid + [v for k in [componentize(i) for i in param_grid] for v in k]
print(param_grid)
for p in param_grid:
	print(p)
	k = keysFromInd(p)
	for bm in ['401', '429']:
		# Remove previous run
		call(f'rm -rf {dir_output}/TEMP/*', shell=True)
		# Call for 429 benchmark
		if bm == '429':
			call(f'{dir_gem5}/build/X86/gem5.opt -d {dir_output}/TEMP {dir_gem5}/configs/example/se.py -I 500000000 -c {dir_spec}/429.mcf/src/benchmark -o {dir_spec}/429.mcf/data/inp.in --cpu-type=timing --caches --l2cache {paramsFromKeys(k)}', shell=True)
		elif bm == '401':
			call(f'{dir_gem5}/build/X86/gem5.opt -d {dir_output}/TEMP {dir_gem5}/configs/example/se.py -I 500000000 -c {dir_spec}/401.bzip/src/benchmark -o {dir_spec}/401.bzip/data/input.program --cpu-type=timing --caches --l2cache {paramsFromKeys(k)}', shell=True)
			#call(f'{dir_spec}/401.bzip/run.sh')
		else:
			print('Unknown benchmark')
		# Call for hello world
		#call(f'{dir_gem5}/build/X86/gem5.opt -d {dir_output}/TEMP {dir_gem5}/configs/example/se.py -I 500000000 -c {dir_gem5}/tests/test-progs/hello/bin/x86/linux/hello --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64', shell=True)

		# Copy simulated data to run unique folder
		perm_str = f'Perm_{"_".join([str(i) for i in p])}_{bm}'
		call(f'mkdir {dir_output}/{perm_str}', shell=True)
		call(f'mv -f {dir_output}/TEMP/* {dir_output}/{perm_str}/', shell=True)

		#resFile = open(f'{dir_output}/TEMP/stats.txt', 'r')
		#regex_row = re.compile('([^ \t\n]+)[ \n\t]+([^ \t\n]+)[ \n\t]+([^ \t\n]+)')
		#d = {'' if r is None else r.group(1): '' if r is None else r.group(2) for r in [regex_row.match(l) for l in resFile.read().splitlines()]}
		#print(f'Instr cache miss: {d["system.cpu.icache.overall_miss_rate::total"]}, Data cache miss: {d["system.cpu.dcache.overall_miss_rate::total"]}, L2 Miss rate: {d["system.l2.overall_miss_rate::total"]}')

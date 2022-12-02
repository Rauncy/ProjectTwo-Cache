from subprocess import call
from datetime import datetime
import os

homeDir = "/home/010/j/jg/jgi220000"
instructionCount = 500000000


def benchmark429Run(instrCount, l1dSize, l1iSize, l2Size, l1dAssoc, l1iAssoc, l2Assoc, cacheline, dirName):
    print("----429 run----")
    currentTime = datetime.now()
    currentTimeString = currentTime.strftime('%T.%f')[:-3]
    print(" Start time 429 run =" + currentTimeString + "\n")
    # Build string
    deleteString = 'rm -r ' + homeDir + '/m5out/*'
    # Delete previous results
    call(deleteString , shell=True)

    # Build directory change string
    dirChangeString = homeDir + "/Project1_SPEC/429.mcf/"
    # Go to benchmark directory
    os.chdir(dirChangeString)

    # Build string
    benchmarkRunString = 'time ' + homeDir + '/gem5/build/X86/gem5.opt -d ~/m5out ' + homeDir + '/gem5/configs/example/se.py -c ./src/benchmark -o ./data/inp.in -I ' + str(instrCount) +' '
    benchmarkRunString += '--cpu-type=timing --caches --l2cache --l1d_size='+str(l1dSize)+' --l1i_size='+str(l1iSize)+' --l2_size='+str(l2Size)+' --l1d_assoc='+str(l1dAssoc)+' --l1i_assoc='+str(l1iAssoc)+' --l2_assoc='+str(l2Assoc)+' --cacheline_size='+str(cacheline)

    print(benchmarkRunString)

    # Run benchmark
    call(benchmarkRunString , shell=True)

    # Move results to save place
    tempResultsDir = homeDir + "/m5out/"
    finalResultsDir = homeDir + "/AltResults/" + dirName
    storeResultsString = 'mv "'+ tempResultsDir+ '" "' + finalResultsDir + '"'
    # print(storeResultsString)
    call(storeResultsString , shell=True)

    # Record end time
    currentTime = datetime.now()
    currentTimeString = currentTime.strftime('%T.%f')[:-3]
    print(" End time 429 run =" + currentTimeString + "\n")

def benchmark401Run(instrCount, l1dSize, l1iSize, l2Size, l1dAssoc, l1iAssoc, l2Assoc, cacheline, dirName):

    print("----401 run----")
    currentTime = datetime.now()
    currentTimeString = currentTime.strftime('%T.%f')[:-3]
    print(" Start time 401 run =" + currentTimeString + "\n")
    # Build string
    deleteString = 'rm -r ' + homeDir + '/m5out/*'
    # Delete previous results
    call(deleteString , shell=True)

    # Build directory change string
    dirChangeString = homeDir + "/Project1_SPEC/401.bzip2/"
    # Go to benchmark directory
    os.chdir(dirChangeString)

    # Build string
    benchmarkRunString = 'time ' + homeDir + '/gem5/build/X86/gem5.opt -d ~/m5out ' + homeDir + '/gem5/configs/example/se.py -c ./src/benchmark -o "./data/input.program 10" -I ' + str(instrCount) +' '
    benchmarkRunString += '--cpu-type=timing --caches --l2cache --l1d_size='+str(l1dSize)+' --l1i_size='+str(l1iSize)+' --l2_size='+str(l2Size)+' --l1d_assoc='+str(l1dAssoc)+' --l1i_assoc='+str(l1iAssoc)+' --l2_assoc='+str(l2Assoc)+' --cacheline_size='+str(cacheline)

    print(benchmarkRunString)

    # Run benchmark
    call(benchmarkRunString , shell=True)

    # Move results to save place
    tempResultsDir = homeDir + "/m5out/"
    finalResultsDir = homeDir + "/AltResults/" + dirName
    storeResultsString = 'mv "'+ tempResultsDir+ '" "' + finalResultsDir + '"'
    # print(storeResultsString)
    call(storeResultsString , shell=True)

    # Record end time
    currentTime = datetime.now()
    currentTimeString = currentTime.strftime('%T.%f')[:-3]
    print(" End time 401 run =" + currentTimeString + "\n")



print("Starting Cache gauntlet")


# Calculate start time
startTime = datetime.now()
startTimeString = startTime.strftime('%T.%f')[:-3]
# Write start time to report
print("Start Time =" + startTimeString + "\n")

# Defining medium as default
# L1D Size = 128kB
# L1I Size = 128kB
# L2 Size = 1MB
# Cache line  = 64
# L1D Associativity = 2
# L1 Associativity = 2
# L2 Associativity = 1

print("Medium Baseline Measurement\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 64, "Baseline-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 64, "Baseline-Configuration401")

# Vary L1D Size 1-128kb
print("============L1D SIZE CONFIG============\n")
# print("=========L1D = 1KB=========\n")
# # benchmark429Run(instructionCount, "1kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-1KB-Configuration429")
# # benchmark401Run(instructionCount, "1kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-1KB-Configuration401")

# # print("=========L1D = 2KB=========\n")
# # benchmark429Run(instructionCount, "2kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-2KB-Configuration429")
# # benchmark401Run(instructionCount, "2kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-2KB-Configuration401")

# print("=========L1D = 4KB=========\n")
# # benchmark429Run(instructionCount, "4kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-4KB-Configuration429")
benchmark401Run(instructionCount, "4kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-4KB-Configuration401")

print("=========L1D = 8KB=========\n")
benchmark429Run(instructionCount, "8kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-8KB-Configuration429")
benchmark401Run(instructionCount, "8kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-8KB-Configuration401")

print("=========L1D = 16KB=========\n")
benchmark429Run(instructionCount, "16kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-16KB-Configuration429")
benchmark401Run(instructionCount, "16kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-16KB-Configuration401")

print("=========L1D = 32KB=========\n")
benchmark429Run(instructionCount, "32kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-32KB-Configuration429")
benchmark401Run(instructionCount, "32kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-32KB-Configuration401")

print("=========L1D = 64KB=========\n")
benchmark429Run(instructionCount, "64kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-64KB-Configuration429")
benchmark401Run(instructionCount, "64kB", "128kB", "1MB", 2, 2, 1, 64, "L1D-64KB-Configuration401")




# Vary L1I Size 1kB-128kB
print("============L1I SIZE CONFIG============\n")
print("=========L1I = 1KB=========\n")
benchmark429Run(instructionCount, "128kB", "1kB", "1MB", 2, 2, 1, 64, "L1I-1KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "1kB", "1MB", 2, 2, 1, 64, "L1I-1KB-Configuration401")

print("=========L1I = 2KB=========\n")
benchmark429Run(instructionCount, "128kB", "2kB", "1MB", 2, 2, 1, 64, "L1I-2KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "2kB", "1MB", 2, 2, 1, 64, "L1I-2KB-Configuration401")

print("=========L1I = 4KB=========\n")
benchmark429Run(instructionCount, "128kB", "4kB", "1MB", 2, 2, 1, 64, "L1I-4KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "4kB", "1MB", 2, 2, 1, 64, "L1I-4KB-Configuration401")

print("=========L1I = 8KB=========\n")
benchmark429Run(instructionCount, "128kB", "8kB", "1MB", 2, 2, 1, 64, "L1I-8KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "8kB", "1MB", 2, 2, 1, 64, "L1I-8KB-Configuration401")

print("=========L1I = 16KB=========\n")
benchmark429Run(instructionCount, "128kB", "16kB", "1MB", 2, 2, 1, 64, "L1I-16KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "16kB", "1MB", 2, 2, 1, 64, "L1I-16KB-Configuration401")

print("=========L1I = 32KB=========\n")
benchmark429Run(instructionCount, "128kB", "32kB", "1MB", 2, 2, 1, 64, "L1I-32KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "32kB", "1MB", 2, 2, 1, 64, "L1I-32KB-Configuration401")

print("=========L1I = 64KB=========\n")
benchmark429Run(instructionCount, "128kB", "64kB", "1MB", 2, 2, 1, 64, "L1I-64KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "64kB", "1MB", 2, 2, 1, 64, "L1I-64KB-Configuration401")



# Vary L2Size (1KB - 1MB)
print("============L2 SIZE CONFIG============\n")
print("=========L2 = 1KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1kB", 2, 2, 1, 64, "L2-1KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1kB", 2, 2, 1, 64, "L2-1KB-Configuration401")

print("=========L2 = 2KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "2kB", 2, 2, 1, 64, "L2-2KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "2kB", 2, 2, 1, 64, "L2-2KB-Configuration401")

print("=========L2 = 4KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "4kB", 2, 2, 1, 64, "L2-4KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "4kB", 2, 2, 1, 64, "L2-4KB-Configuration401")

print("=========L2 = 8KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "8kB", 2, 2, 1, 64, "L2-8KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "8kB", 2, 2, 1, 64, "L2-8KB-Configuration401")

print("=========L2 = 16KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "16kB", 2, 2, 1, 64, "L2-16KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "16kB", 2, 2, 1, 64, "L2-16KB-Configuration401")

print("=========L2 = 32KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "32kB", 2, 2, 1, 64, "L2-32KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "32kB", 2, 2, 1, 64, "L2-32KB-Configuration401")

print("=========L2 = 64KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "64kB", 2, 2, 1, 64, "L2-64KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "64kB", 2, 2, 1, 64, "L2-64KB-Configuration401")

print("=========L2 = 128KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "128kB", 2, 2, 1, 64, "L2-128KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "128kB", 2, 2, 1, 64, "L2-128KB-Configuration401")

print("=========L2 = 256KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "256kB", 2, 2, 1, 64, "L2-256KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "128kB", 2, 2, 1, 64, "L2-256KB-Configuration401")

print("=========L2 = 512KB=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "512kB", 2, 2, 1, 64, "L2-512KB-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "512kB", 2, 2, 1, 64, "L2-512KB-Configuration401")




# Vary Cacheline 8-512
print("============CACHELINE CONFIG============\n")
print("=========CACHELINE = 8B=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 8, "Cacheline-8B-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 8, "Cacheline-8B-Configuration401")

print("=========CACHELINE = 16B=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 16, "Cacheline-16B-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 16, "Cacheline-16B-Configuration401")

print("=========CACHELINE = 32B=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 32, "Cacheline-32B-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 32, "Cacheline-32B-Configuration401")

print("=========CACHELINE = 128B=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 128, "Cacheline-128B-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 128, "Cacheline-128B-Configuration401")

print("=========CACHELINE = 256B=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 256, "Cacheline-256B-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 256, "Cacheline-256B-Configuration401")

print("=========CACHELINE = 512B=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 512, "Cacheline-512B-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1, 512, "Cacheline-512B-Configuration401")




# # Vary L1D Associativity 1-8
print("============L1D ASSOC CONFIG============\n")
print("=========L1D ASSOC = 1=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 1, 2, 1, 64, "L1DAssoc-1-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 1, 2, 1, 64, "L1DAssoc-1-Configuration401")

print("=========L1D ASSOC = 4=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 4, 2, 1, 64, "L1DAssoc-4-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 4, 2, 1, 64, "L1DAssoc-4-Configuration401")

print("=========L1D ASSOC = 8=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 8, 2, 1, 64, "L1DAssoc-8-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 8, 2, 1, 64, "L1DAssoc-8-Configuration401")



# # Vary L1I Associativity 1-8
print("============L1I ASSOC CONFIG============\n")
print("=========L1I ASSOC = 1=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 1, 1, 64, "L1IAssoc-1-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 1, 1, 64, "L1IAssoc-1-Configuration401")

print("=========L1I ASSOC = 4=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 4, 1, 64, "L1IAssoc-4-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 4, 1, 64, "L1IAssoc-4-Configuration401")

print("=========L1I ASSOC = 8=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 8, 1, 64, "L1IAssoc-8-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 8, 1, 64, "L1IAssoc-8-Configuration401")


# # Vary L1I Associativity 1-8
print("============L2 ASSOC CONFIG============\n")
print("=========L2 ASSOC = 2=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 2, 64, "L2Assoc-2-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 2, 64, "L2Assoc-2-Configuration401")

print("=========L2 ASSOC = 4=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 4, 64, "L2Assoc-4-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 4, 64, "L2Assoc-4-Configuration401")

print("=========L2 ASSOC = 8=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 8, 64, "L2Assoc-8-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 8, 64, "L2Assoc-8-Configuration401")

print("=========L2 ASSOC = 16=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 16, 64, "L2Assoc-16-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 16, 64, "L2Assoc-16-Configuration401")

print("=========L2 ASSOC = 32=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 32, 64, "L2Assoc-32-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 32, 64, "L2Assoc-32-Configuration401")

print("=========L2 ASSOC = 64=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 64, 64, "L2Assoc-64-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 64, 64, "L2Assoc-64-Configuration401")

print("=========L2 ASSOC = 128=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 128, 64, "L2Assoc-128-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 128, 64, "L2Assoc-128-Configuration401")

print("=========L2 ASSOC = 256=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 256, 64, "L2Assoc-256-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 256, 64, "L2Assoc-256-Configuration401")

print("=========L2 ASSOC = 512=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 512, 64, "L2Assoc-512-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 512, 64, "L2Assoc-512-Configuration401")

print("=========L2 ASSOC = 1024=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1024, 64, "L2Assoc-1024-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 1024, 64, "L2Assoc-1024-Configuration401")

print("=========L2 ASSOC = 2048=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 2048, 64, "L2Assoc-2048-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 2048, 64, "L2Assoc-2048-Configuration401")

print("=========L2 ASSOC = 4096=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 4096, 64, "L2Assoc-4096-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 4096, 64, "L2Assoc-4096-Configuration401")

print("=========L2 ASSOC = 8192=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 8192, 64, "L2Assoc-8192-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 8192, 64, "L2Assoc-8192-Configuration401")

print("=========L2 ASSOC = 16384=========\n")
benchmark429Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 16384, 64, "L2Assoc-16384-Configuration429")
benchmark401Run(instructionCount, "128kB", "128kB", "1MB", 2, 2, 16384, 64, "L2Assoc-16384-Configuration401")



# Calculate end time
endTime = datetime.now()
endTimeString = endTime.strftime('%T.%f')[:-3]
print("End Time =" + endTimeString + "\n")
# Calculate elapsed time
elapsedTime = endTime - startTime
print("Elapsed Time =" + str(elapsedTime) + "\n")


from subprocess import call
from datetime import datetime
import os

homeDir = "/home/010/j/jg/jgi220000"
instructionCount = 500000


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
    finalResultsDir = homeDir + "/Results/" + dirName
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
    finalResultsDir = homeDir + "/Results/" + dirName
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
# L1D Size = 64kB
# L1I Size = 64kB
# L2 Size = 512kB
# Cache line  = 64B - Issues with cacheline at 256. Using 16, 32, 64, and 128 instead
# L1D Associativity = 4
# L1 Associativity = 4
# L2 Associativity = 4096

# Vary L1D Size (1kB, 64kB, 128kB)
#  benchmark429Run(instrCount, l1dSize, l1iSize, l2Size, l1dAssoc, l1iAssoc, l2Assoc, cacheline, dirName):
    # Low L1D Size (1kB)
print("============L1D SIZE CONFIG============\n")
print("=========LOw=========\n")
benchmark429Run(instructionCount, "1kB", "64kB", "512kB", 4, 4, 4096, 64, "LowL1DConfiguration429")
benchmark401Run(instructionCount, "1kB", "64kB", "512kB", 4, 4, 4096, 64, "LowL1DConfiguration401")

#     # Medium L1D Size (64kB)
print("=========MED=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 4096, 64, "MedL1DConfiguration429")
benchmark401Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 4096, 64, "MedL1DConfiguration401")

# print("=========HI=========\n")
    # High L1D Size (128kB)
benchmark429Run(instructionCount, "128kB", "64kB", "512kB", 4, 4, 4096, 64, "HiL1DConfiguration429")
benchmark401Run(instructionCount, "128kB", "64kB", "512kB", 4, 4, 4096, 64, "HiL1DConfiguration401")


# Vary L1I Size (1kB, 64kB, 128kB)
# benchmark429Run(instrCount, l1dSize, l1iSize, l2Size, l1dAssoc, l1iAssoc, l2Assoc, cacheline, dirName):
    # Low L1I Size (1kB)
print("============L1I SIZE CONFIG============\n")
print("=========LOw=========\n")
benchmark429Run(instructionCount, "64kB", "1kB", "512kB", 4, 4, 4096, 64, "LowL1IConfiguration429")
benchmark401Run(instructionCount, "64kB", "1kB", "512kB", 4, 4, 4096, 64, "LowL1IConfiguration401")

    # High L1I Size (128kB)
print("=========HI=========\n")
benchmark429Run(instructionCount, "64kB", "128kB", "512kB", 4, 4, 4096, 64, "HiL1IConfiguration429")
benchmark401Run(instructionCount, "64kB", "128kB", "512kB", 4, 4, 4096, 64, "HiL1IConfiguration401")



# Vary L2Size (256kB, 512kB, 1MB)
# benchmark429Run(instrCount, l1dSize, l1iSize, l2Size, l1dAssoc, l1iAssoc, l2Assoc, cacheline, dirName):
    # Low L2Size Size (256kB)
print("============L2 SIZE CONFIG============\n")
print("=========LOw=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "256kB", 4, 4, 4096, 64, "LowL2Configuration429")
benchmark401Run(instructionCount, "64kB", "64kB", "256kB", 4, 4, 4096, 64, "LowL2Configuration401")

    # High L2Size Size (1MB)
print("=========HI=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "1MB", 4, 4, 4096, 64, "HiL2Configuration429")
benchmark401Run(instructionCount, "64kB", "64kB", "1MB", 4, 4, 4096, 64, "HiL2Configuration401")

# Vary Cacheline (8, 64, 128)
# benchmark429Run(instrCount, l1dSize, l1iSize, l2Size, l1dAssoc, l1iAssoc, l2Assoc, cacheline, dirName):
    # Low Cacheline Size (32)
print("============CACHELINE CONFIG============\n")
print("=========LOw=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 4096, 8, "LowCachelineConfiguration429")
benchmark401Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 4096, 8, "LowCachelineConfiguration401")

    # High Cacheline Size (128) 
print("=========HI=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 4096, 128, "HiCachelineConfiguration429")
benchmark401Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 4096, 128,"HiCachelineConfiguration401")




# # Vary L1D Associativity (1, 4, 8)
# # benchmark429Run(instrCount, l1dSize, l1iSize, l2Size, l1dAssoc, l1iAssoc, l2Assoc, cacheline, dirName):
    # Low L1D Associativity (1)
print("============L1D ASSOC CONFIG============\n")
print("=========LOw=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 1, 4, 4096, 64, "LowL1DAssocConfiguration429")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 1, 4, 4096, 64, "LowL1DAssocConfiguration401")

    # High L1D Associativity(8)
print("=========HI=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 8, 4, 4096, 64, "HiL1DAssocConfiguration429")
benchmark401Run(instructionCount, "64kB", "64kB", "512kB", 8, 4, 4096, 64, "HiL1DAssocConfiguration401")



# # Vary L1 Associativity (1, 4, 8)
# benchmark429Run(instrCount, l1dSize, l1iSize, l2Size, l1dAssoc, l1iAssoc, l2Assoc, cacheline, dirName):
    # Low L1 Associativity (1)
print("============L1I ASSOC CONFIG============\n")
print("=========LOw=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 4, 1, 4096, 64, "LowL1IAssocConfiguration429")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 4, 1, 4096, 64, "LowL1IAssocConfiguration401")

    # High L1 Associativity(8)
print("=========HI=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 4, 8, 4096, 64, "HiL1IAssocConfiguration429")
benchmark401Run(instructionCount, "64kB", "64kB", "512kB", 4, 8, 4096, 64, "HiL1IAssocConfiguration401")

# # Vary L2 Associativity (1, 4096, 8192 )
# benchmark429Run(instrCount, l1dSize, l1iSize, l2Size, l1dAssoc, l1iAssoc, l2Assoc, cacheline, dirName):
    # Low L2 Associativity (1)
print("============L2 ASSOC CONFIG============\n")
print("=========LOw=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 1, 64, "LowL2AssocConfiguration429")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 1, 64, "LowL2AssocConfiguration401")

    # High L2 Associativity(8192)
print("=========HI=========\n")
benchmark429Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 8192, 64, "HiL2AssocConfiguration429")
benchmark401Run(instructionCount, "64kB", "64kB", "512kB", 4, 4, 8192, 64,"HiL2AssocConfiguration401")



# Calculate end time
endTime = datetime.now()
endTimeString = endTime.strftime('%T.%f')[:-3]
print("End Time =" + endTimeString + "\n")
# Calculate elapsed time
elapsedTime = endTime - startTime
print("Elapsed Time =" + str(elapsedTime) + "\n")


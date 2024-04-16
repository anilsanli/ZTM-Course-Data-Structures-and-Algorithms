import time


def find_nemo(fish):
    start_time = time.time()
    for item in fish:
        if item == 'nemo':
            print('Found Nemo!')
    end_time = time.time()
    print("Finding Nemo took " + str((end_time - start_time) * 1000) + " milliseconds.")


fish = ['dory', 'bruce', 'marlin', 'nemo']
nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo'] * 10

find_nemo(everyone)

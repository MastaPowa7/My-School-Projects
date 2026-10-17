# credit to u/gryndil for the formula https://www.reddit.com/r/geometrydash/comments/1tekw0i/idea_if_you_have_a_level_in_2_runs_we_should/
# made by MastaPowa7
def addRuns(index = 0, total = 0):
  total += runs[index] - runs[index + 1]
  if index != len(runs) - 2:
    index += 2
    return addRuns(index, total)
  else:
    return total

runs = [40,35,78,70] # first index is your pb from 0. Every odd numbered index is the starting percentage of your run, and every even numbered index is the ending percentage of your run. The final index is your last run to 100. Array must be even or it will not work.
totalRuns = len(runs) // 2 + 1 # how many runs you did, calculated based on the number of runs in the runs array.
runCount = totalRuns - (addRuns()) / 100
print(f"Completed the level in {runCount:.2f} runs.")

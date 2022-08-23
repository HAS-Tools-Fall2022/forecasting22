# Forecast evaluation <!-- omit in toc -->
This folder contains the python scripts for doing forecast evaluation. This readme contains the instructions for what to do when it is your week to be the evaluator. NOTE I strongly recommend you start looking over these instructions and planning the script you will write several weeks in advance so that you can ask for help if needed. 
____
## Table of Contents:<!-- omit in toc -->
- [Evaluation Instructions](#evaluation-instructions)
  - [Pre-Evaluation](#pre-evaluation)
  - [Evaluation](#evaluation)
  - [Post-Evaluation](#post-evaluation)
  - [Submission](#submission)

___
<a name="evaluation"></a>
## Evaluation Instructions

### Pre-Evaluation
I recommend you start these pre-evaluation steps *several* weeks in advance so you have time to ask questions. 

1. **Install necessary Packages** To run these scripts you will need to first add the following to your hastools conda environment by doing the following from your shell:

 ```
 conda activate hastools
 conda install pip
 pip install dataretrieval

 conda install -c conda-forge seaborn
 ```

2. **Understand the Work Flow** Many python scripts and data inputs are used to evaluate forecasts. Make sure you understand (generally) what each script is doing. Also read all of the instructions in advance so you will know what you are going to be doing. 

3. **Plan your bonus script Approach** Come up with an idea for how you want to assign bonus points and plan out how to do it. If you have questions come to office hours so I can help. Note you can start this planning several weeks in advance and can start writing your bonus script too. Just note that you have to do somethign unique so you will need to see what the week before you is doing before you finalize your plan. 

### Evaluation
1. **Score the 1- and 2- week forecasts (after noon on Monday)***: Pull the latest updates from everyone and run the weekly forecast evaluation. Using the `score_weekly.py` script. You will need to update the following the `forecast_week` to run this script. You can look that up in the `Seasonal_Forecast_Dates.pdf` file. For your week `#` this will create the `forecast_week#_results.csv` file in the directory `weekly_results` and the `Forecast_Summary_weekx.png` plot in the `weekly_plots` directory. Look at these results and the results that get printed from the script to see how everyone did.

2. **Assign Bonus points** After you do the scoring decide how you will assign bonus points. You should write your  own analysis script to determine how to assign bonus points you can save this  as  `./bonus/Bonus_wk#.py`. **IMPORTANT: Your bonus script should end with the function `write_bonus` from the `eval_functions.py`.** This function writes the bonus point winners the file `bonus_week#.csv` in the directory `weekly_results`. See the bottom of the `Bonus_wk1.py` and `Bonus_wk2.py` scripts for examples of how to do this.  **NOTE** You will want to start a new interactive session when you run your bonus script in order for the working directory to reset. 

3. **Calculate total scores** Run `Scoreboard.py` script to see the overall rankings and total scores. This will update `scoreboard.csv` and `score_details.csv`.

4. **Run some analysis on the forecast competition so far** Run `Forecast_analysis.py` to create some timeseries plots of the foreast competition so far. This script will create `Forecast_Boxplots_weekx.png` and `RankingEvolution_weekx.png` in the `weekly_plots` folder.  **NOTE:** some fo the functionality in this script may be useful for your bonus script writing. 

5. **Compare the forecasts to 'truth', to date** After using `Get_Observations.py`. Update the week number in `forecast_analysis.py` and run the script to review the class performance of weekly forecasts to date. The `forecast_analysis.py` script will produce many types of graphs of everyone's 1 week and 2 week forecasts, so we can review everyone's performance to date.

### Post-Evaluation
1. **Update the scoreboard** update the scoreboard.md file in the main directory of this folder with the points you applied this week and the updated overall scores. The information you need will come out of the print statements when you run `score_weekly.py` and `/weekly_results/scoreboard_weekk.csv` will have the total overall points and rankings summarized for you
   
2. **Create a Presentation for class**: You will present the results from this weeks evaluation in class on Tuesday. Plan on taking ~10 minutes for your presentation. Your presentation must include the following: 
   - The observed flow for the week you were judging
   - Some graphs of the foreacasts made (note you can use the ones that generate automatically or create your own)
   - Justification for how you assigned your bonus points and an explanation for how you did it in python
   - An explanation of one block of code from the forecast evaluation scripts that you ran (I recommend choosing a block of code that includes somethign we have covered already in class)
   - The points awarded this week and the overall rankings 

**NOTE:** *ALL of the analysis that you do should be contained in your bonus points script. Do not add your individualized analysis to the main evaluation scripts.* 

### Submission
You will be graded on your Bonus point assignment script and your forecast presenation. 
1. Once you are done stage-commit-and push your changes to update the forecast repo. 
2. Email your forecast presentation to Laura.

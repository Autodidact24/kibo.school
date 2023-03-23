# Measuring CO2 Emmission

You are working at a Climate Tech startup. You are tasked with creating a presentation for your client showing historical CO2 emmission trends.

## Your Task

You will write program to do the following:
1. Fetch data from [Global-Warming.org](https://global-warming.org/)'s CO2 API.
This API provides on a quasi-daily basis, the amount of carbon dioxide (CO2) in the atmosphere from 2010.01.01 to the present. It is expressed as a mole fraction in dry air, parts per million (ppm). Fetch this endpoint https://global-warming.org/api/co2-api and you will get the info in JSON format.

2. You will parse the JSON response from the API and store the data in a CSV.

## Starter Code

The starter code in `log_analyzer.py` has most of the `analyze_log` function and 
helper functions built out. It also has code to read a file and run the analysis
when the program is run from the command line. When running the program, you 
can pass in an input file, and an optional output file to write the results.

Examples:
```
python log_analyzer.py result_logs/test_results.log

python log_analyzer.py result_logs/test_results_3.log statistics_output.txt
```

## Expected Results

The output for your program should look like this:

```
Number of tests: 15
Most used type of tests: Performance
Tests related to "component": 10

Failures:
Type            Count
Performance     5
System          6
Functional      8

```

## Testing

First, run your program manually to check that the output makes sense. Pass in
some of the files in the `result_logs/` folder to check that the output matches
what you expect.

Then, run the automated tests to confirm that your solution is correct.

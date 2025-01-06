# AB Test Sample Size Calculator

## Project Overview
This is a Python tool for calculating the minimum sample size required for AB testing, based on statistical power analysis. Supports both Chinese and English interfaces.

## Key Features
- Calculate minimum sample size for AB testing
- Supports bilingual interface (Chinese/English)
- User-friendly graphical interface
- Real-time calculation results
- Detailed parameter explanations

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run the program: `python main.py`
3. Input parameters:
   - Baseline conversion rate (0-1)
   - Minimum detectable effect (%)
   - Statistical power (0-1)
   - Significance level (0-1)
4. Click "Calculate Sample Size" button to view results

## Parameter Explanations
- **Baseline Conversion Rate**: Current conversion rate
- **Minimum Detectable Effect**: Minimum change percentage you want to detect
- **Statistical Power**: Probability of detecting a true difference
- **Significance Level**: Probability of Type I error

## Example
Assumptions:
- Current conversion rate: 0.55
- Minimum detectable effect: 4%
- Statistical power: 0.8
- Significance level: 0.05

Calculation result: Each test group requires approximately 8,027 samples

## Requirements
- Python 3.6+
- tkinter
- scipy
- numpy

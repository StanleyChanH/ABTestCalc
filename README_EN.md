# AB Test Sample Size Calculator

A Python GUI application for calculating the minimum sample size required for AB testing.

## Features

- Calculate minimum sample size for AB testing
- User-friendly graphical interface
- Customizable parameters:
  - Baseline conversion rate
  - Minimum detectable effect
  - Statistical power
  - Significance level
- Automatic result formatting
- Detailed input validation

## Usage

1. Download and install Python 3.x
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Parameters

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| Baseline Conversion Rate | Current conversion rate | 0.55 | 0-1 |
| Minimum Detectable Effect | Minimum change to detect effect | 4% | 0-100% |
| Statistical Power | Probability of detecting true difference | 0.8 | 0-1 |
| Significance Level | Type I error probability | 0.05 | 0-1 |

## Calculation Formula

The sample size is calculated using:

```
n = 2 * ((Zα + Zβ)^2 * p(1-p)) / δ^2
```

Where:
- Zα: Z-value for significance level
- Zβ: Z-value for statistical power
- p: Baseline conversion rate
- δ: Minimum detectable effect

## Packaging

Package as executable using PyInstaller:

```bash
pyinstaller --onefile --windowed --add-data "icon.ico;." --icon=icon.ico main.py
```

## License

MIT License

## Contributing

Issues and pull requests are welcome

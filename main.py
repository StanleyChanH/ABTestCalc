import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import scipy.stats as stats

# 语言资源
LANGUAGES = {
    'zh': {
        'title': 'AB测试样本数计算器',
        'baseline': '目标转化率基线 (0-1):',
        'effect': '最小可检测效果（判断实验有效性的最小变化）(%):',
        'power': '统计功效 (0-1):',
        'alpha': '显著性水平 (0-1):',
        'calculate': '计算样本量',
        'result': '每个实验组所需样本量: {result:,}',
        'info': '说明：\n1. 样本量表示每个实验组需要的最小样本数\n2. 总样本量 = 实验组样本量 × 组数',
        'error': {
            'baseline': '[必填]目标转化率基线必须在0到1之间。',
            'effect': '[必填]最小可检测效果（判断实验有效性的最小变化）必须在0到100之间。',
            'power': '[默认]统计功效必须在0到1之间。',
            'alpha': '[默认]显著性水平必须在0到1之间。'
        }
    },
    'en': {
        'title': 'AB Test Sample Size Calculator',
        'baseline': 'Baseline Conversion Rate (0-1):',
        'effect': 'Minimum Detectable Effect (%):',
        'power': 'Statistical Power (0-1):',
        'alpha': 'Significance Level (0-1):',
        'calculate': 'Calculate Sample Size',
        'result': 'Required sample size per group: {result:,}',
        'info': 'Notes:\n1. Sample size represents the minimum required per group\n2. Total sample size = group size × number of groups',
        'error': {
            'baseline': '[Required] Baseline conversion rate must be between 0 and 1.',
            'effect': '[Required] Minimum detectable effect must be between 0 and 100.',
            'power': '[Default] Statistical power must be between 0 and 1.',
            'alpha': '[Default] Significance level must be between 0 and 1.'
        }
    }
}

current_lang = 'zh'  # 默认语言

def change_language(lang):
    global current_lang
    current_lang = lang
    update_ui_text()

def calculate_sample_size():
    try:
        baseline_conversion_rate = float(entry_baseline.get())
        min_detectable_effect = float(entry_effect.get())
        power = float(entry_power.get())
        alpha = float(entry_alpha.get())

        if not (0 < baseline_conversion_rate < 1):
            raise ValueError(LANGUAGES[current_lang]['error']['baseline'])
        if not (0 < min_detectable_effect <= 100):
            raise ValueError(LANGUAGES[current_lang]['error']['effect'])
        if not (0 < power < 1):
            raise ValueError(LANGUAGES[current_lang]['error']['power'])
        if not (0 < alpha < 1):
            raise ValueError(LANGUAGES[current_lang]['error']['alpha'])

        delta = baseline_conversion_rate * (min_detectable_effect / 100)
        z_alpha = stats.norm.ppf(1 - alpha / 2)
        z_beta = stats.norm.ppf(power)
        p_hat = baseline_conversion_rate * (1 - baseline_conversion_rate)
        n = 2 * ((z_alpha + z_beta) ** 2 * p_hat / delta ** 2)

        result = int(round(n))
        label_result.config(
            text=LANGUAGES[current_lang]['result'].format(result=result),
            font=("Arial", 12, "bold"),
            foreground="#0078D7",
            background="#F0F0F0",
            padding=10
        )
    except ValueError as e:
        messagebox.showerror("无效输入", str(e))

def update_ui_text():
    root.title(LANGUAGES[current_lang]['title'])
    label_baseline.config(text=LANGUAGES[current_lang]['baseline'])
    label_effect.config(text=LANGUAGES[current_lang]['effect'])
    label_power.config(text=LANGUAGES[current_lang]['power'])
    label_alpha.config(text=LANGUAGES[current_lang]['alpha'])
    button_calculate.config(text=LANGUAGES[current_lang]['calculate'])
    label_info.config(text=LANGUAGES[current_lang]['info'])

# 创建主窗口
root = tk.Tk()
root.title(LANGUAGES[current_lang]['title'])
root.geometry("500x500")
root.resizable(False, False)

# 设置窗口图标
try:
    import sys
    import os
    if getattr(sys, 'frozen', False):
        # 打包后从临时目录加载图标
        base_path = sys._MEIPASS
    else:
        # 开发时从当前目录加载图标
        base_path = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(base_path, 'icon.ico')
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"加载图标失败: {e}")

# 使用ttk样式
style = ttk.Style()
style.configure('TFrame', background='#ffffff')
style.configure('TLabel', background='#ffffff', font=('Arial', 10))
style.configure('TEntry', font=('Arial', 10), padding=5)
style.configure('TButton', font=('Arial', 10, 'bold'), padding=5)

# 创建主框架
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# 创建并放置标签和输入框
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=10)

# 添加语言选择
language_frame = ttk.Frame(main_frame)
language_frame.pack(fill=tk.X, pady=5)

language_var = tk.StringVar(value=current_lang)
language_menu = ttk.Combobox(language_frame, 
                            textvariable=language_var, 
                            values=['zh', 'en'],
                            state='readonly')
language_menu.bind('<<ComboboxSelected>>', lambda e: change_language(language_var.get()))
language_menu.pack(side=tk.RIGHT)

ttk.Label(language_frame, text="Language:").pack(side=tk.RIGHT, padx=5)

# 创建并放置标签和输入框
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=10)

label_baseline = ttk.Label(input_frame)
label_baseline.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_baseline = ttk.Entry(input_frame, width=20)
entry_baseline.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

label_effect = ttk.Label(input_frame)
label_effect.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_effect = ttk.Entry(input_frame, width=20)
entry_effect.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

label_power = ttk.Label(input_frame)
label_power.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_power = ttk.Entry(input_frame, width=20)
entry_power.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

label_alpha = ttk.Label(input_frame)
label_alpha.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_alpha = ttk.Entry(input_frame, width=20)
entry_alpha.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

# 设置默认值
entry_baseline.insert(0, "0.55")
entry_effect.insert(0, "4")
entry_power.insert(0, "0.8")
entry_alpha.insert(0, "0.05")

# 创建并放置计算按钮
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10)

button_calculate = ttk.Button(button_frame, text="计算样本量", command=calculate_sample_size, style='Accent.TButton')
button_calculate.pack(pady=10)

# 创建并放置结果显示标签
# 创建并放置结果显示标签
result_frame = ttk.Frame(main_frame, style='Result.TFrame')
result_frame.pack(fill=tk.X, pady=(10, 5), expand=False)

label_result = ttk.Label(result_frame, 
                        text="", 
                        font=("Arial", 12, "bold"),
                        foreground="#0078D7",
                        background="#F0F0F0",
                        padding=15)
label_result.pack(fill=tk.X, expand=True)

# 添加单位说明
info_frame = ttk.Frame(main_frame, padding=(10, 5))
info_frame.pack(fill=tk.X, pady=5, expand=False)

label_info = ttk.Label(info_frame, 
         font=("Arial", 9),
         justify="left",
         wraplength=400)
label_info.pack(fill=tk.X, anchor="w")

# 初始化界面文本
update_ui_text()

# 运行主循环
root.mainloop()

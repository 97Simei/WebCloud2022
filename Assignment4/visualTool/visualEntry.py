#!/usr/bin/env python3

import os
import sys

from typing import Union
import yaml
from visualFunctionDetail import PlotFunction


def plot(input_path, function_type, target_columns, title, plot_type, output_path):
    plot_worker = PlotFunction(
        input_path=input_path,
        title=title,
        function_type=function_type,
        plot_type=plot_type,
        target_columns=target_columns,
        output_path=output_path
    )
    saved_space: str = plot_worker.do_plot()
    return saved_space


def get_env_var(key: str) -> Union[str, None]:
    result = os.environ.get(key, None)
    if result == "None" or result == "" or result == "\"\"":
        return None
    return result


if __name__ == "__main__":
    command = sys.argv[1]
    input_path = get_env_var("INPUT_PATH")
    title = get_env_var("TITLE")
    function_type = get_env_var("FUNCTION_TYPE")
    plot_type = get_env_var("PLOT_TYPE")
    target_columns = get_env_var("TARGET_COLUMNS")
    output_path = get_env_var("OUTPUT_PATH")
    functions = {
        "plot": plot,
    }
    output = functions[command](
        input_path,function_type, target_columns, title, plot_type, output_path)
    print(yaml.dump({"output": output}))

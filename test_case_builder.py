import os
import shutil


def set_inputs(path, inputs):
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(os.path.join(path, "in")):
        os.mkdir(os.path.join(path, "in"))
    for i in range(len(inputs)):
        f = open(os.path.join(path, 'in', f'input{i + 1}.txt'), 'w')
        f.write("\n".join(inputs[i]))
        f.close()


def get_inputs(path):
    inputs = []
    i = 1
    while os.path.exists(os.path.join(path, "in", f"input{i}.txt")):
        with open(os.path.join(path, "in", f"input{i}.txt")) as f:
            inputs += [f.read().split("\n")]
        i += 1
    return inputs


def set_outputs(path, outputs):
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(os.path.join(path, "out")):
        os.mkdir(os.path.join(path, "out"))
    for i in range(len(outputs)):
        f = open(os.path.join(path, 'out', f'output{i + 1}.txt'), 'w')
        f.write("\n".join(outputs[i]))
        f.close()


def get_outputs(path):
    outputs = []
    i = 1
    while os.path.exists(os.path.join(path, "out", f"output{i}.txt")):
        with open(os.path.join(path, "out", f"output{i}.txt")) as f:
            outputs += [f.read().split("\n")]
        i += 1
    return outputs


def build_zip(path):
    shutil.make_archive(path, 'zip', path)

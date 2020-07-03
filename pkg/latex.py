"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
from pylatex import Document, Section
import matplotlib
from matplotlib import rcParams
import matplotlib.pyplot as plt
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}\usepackage{amssymb}'
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True

def renderlatex(formula, fontsize=18, dpi=300, format_='png'):
    """
    Renders LaTeX formula into image.
    """
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, u'${}.format(formula)', fontsize=fontsize)
    buffer_ = io.BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_, bbox_inches='tight', pad_inches=0.0)
    return buffer_.getvalue()

def formula2img(str_latex, out_file, img_size=(5, 3), font_size=16):
    fig = plt.figure(figsize=img_size)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.text(0.5, 0.5, str_latex, fontsize=font_size, verticalalignment='center', horizontalalignment='center')
    plt.savefig(out_file)

def main():
    # doc = Document(default_filepath="basic", documentclass="article")
    # with doc.create(Section("math")):
    #     doc.append(r"$$ \begin{aligned} {8656} &= {1} * {7780} + {876} \\{7780} &= {8} * {876} + {772} \\{876} &= {1} * {772} + {104} \\{772} &= {7} * {104} + {44} \\{104} &= {2} * {44} + {16} \\{44} &= {2} * {16} + {12} \\{16} &= {1} * {12} + {4} \\{12} &= {3} * {4} + {0} \\ \end{aligned} $$ $$ \begin{aligned} {4} &= ({1}) * {16} + ({-1}) * {12} \\ &= ({1}) * {16} + ({-1}) * ({44} - ({2}) * {16}) \\ &= ({-1}) * {44} + ({3}) * {16} \\ &= ({-1}) * {44} + ({3}) * ({104} - ({2}) * {44}) \\ &= ({3}) * {104} + ({-7}) * {44} \\ &= ({3}) * {104} + ({-7}) * ({772} - ({7}) * {104}) \\ &= ({-7}) * {772} + ({52}) * {104} \\ &= ({-7}) * {772} + ({52}) * ({876} - ({1}) * {772}) \\ &= ({52}) * {876} + ({-59}) * {772} \\ &= ({52}) * {876} + ({-59}) * ({7780} - ({8}) * {876}) \\ &= ({-59}) * {7780} + ({524}) * {876} \\ &= ({-59}) * {7780} + ({524}) * ({8656} - ({1}) * {7780}) \\ &= ({524}) * {8656} + ({-583}) * {7780} \\ \end{aligned} $$")
    #
    # doc.generate_pdf(filepath=".")
    # x = r"\usepackage{amsmath}\usepackage{amssymb}\begin{aligned} $ {8656} &= {1} * {7780} + {876} \ {7780} &= {8} * {876} + {772} \ {876} &= {1} * {772} + {104} \{772} &= {7} * {104} + {44} \{104} &= {2} * {44} + {16} \{44} &= {2} * {16} + {12} \{16} &= {1} * {12} + {4} \{12} &= {3} * {4} + {0} \  $\end{aligned} \begin{aligned}$  {4} &= ({1}) * {16} + ({-1}) * {12} \ &= ({1}) * {16} + ({-1}) * ({44} - ({2}) * {16}) \ &= ({-1}) * {44} + ({3}) * {16} \ &= ({-1}) * {44} + ({3}) * ({104} - ({2}) * {44}) \ &= ({3}) * {104} + ({-7}) * {44} \ &= ({3}) * {104} + ({-7}) * ({772} - ({7}) * {104}) \ &= ({-7}) * {772} + ({52}) * {104} \ &= ({-7}) * {772} + ({52}) * ({876} - ({1}) * {772}) \ &= ({52}) * {876} + ({-59}) * {772} \ &= ({52}) * {876} + ({-59}) * ({7780} - ({8}) * {876}) \ &= ({-59}) * {7780} + ({524}) * {876} \ &= ({-59}) * {7780} + ({524}) * ({8656} - ({1}) * {7780}) \ &= ({524}) * {8656} + ({-583}) * {7780} \ $ \end{aligned}"
    # formula2img(x, r".1.png", img_size=(20, 10), font_size=10)


if __name__ == '__main__':
    main()

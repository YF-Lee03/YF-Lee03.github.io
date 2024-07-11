from TexSoup.data import TexNode, TexEnv, TexCmd
from TexSoup import TexSoup

latexMathEnvs1 = ['align', 'equation', 'gather']
latexMathEnvs2 = [x + '*' for x in latexMathEnvs1]
latexMathEnvs = ['\\begin{%s}' % x for x in (latexMathEnvs1 + latexMathEnvs2)]
latexMathEnvs_set = set(latexMathEnvs)

def get_node_text(node):
    return ''.join(list(node.text))

with open('source/Surf2024.tex', 'r') as infile:
    data = infile.read()


def get_node_type(node):
    if isinstance(node, str):
        return 'comment'
    if isinstance(node, TexNode):
        expr = node.expr
        if isinstance(expr, TexCmd):
            return 'cmd'
        elif isinstance(expr, TexEnv):
            return 'env'
        else:
            return 'text'

    return 'unknown'

def if_in_inline_math_mode(envs):
    return '$' in envs

def if_in_display_math_mode(envs):
    envs_set = set(envs)
    itsc = latexMathEnvs_set.intersection(envs_set)
    if len(itsc) > 0:
        return True
    return False

def process_latex_nodes(parent, result, envs):
    for stuff in parent:
        nodeType = get_node_type(stuff)
        if nodeType == 'text':
            result.append(get_node_text(stuff))
        elif nodeType == 'comment':
            result.append(stuff)
        elif nodeType == 'cmd':
            expr = stuff.expr
            if expr.name in ['emph', 'textit']:
                result.append('*{}*'.format(expr.args[0]))
            elif expr.name == 'textbf':
                result.append('**{}**'.format(expr.args[0]))
            elif expr.name == 'header':
                headerLevel = int(expr.args[0])
                headerText = expr.args[1]
                result.append('#' * headerLevel + ' ' + headerText + '\n')
            elif expr.name == 'toind':
                result.append('%{{{}}}%'.format(expr.args[0]))
            elif expr.name == 'href':
                result.append('<a href=\"{}\">{}</a>'.format(expr.args[0], expr.args[1]))
            else:
                result.append(str(stuff))
        elif nodeType == 'env':
            expr = stuff.expr

            if expr.begin == '$':
                fixCash = False
                if not if_in_inline_math_mode(envs):
                    fixCash = True

                if fixCash:
                    result.append('$$')

                envs.append(expr.begin)
                process_latex_nodes(stuff, result, envs)
                envs.pop()

                if fixCash:
                    result.append('$$')
            elif expr.begin in latexMathEnvs:
                fixCash = False

                if not if_in_display_math_mode(envs):
                    fixCash = True

                if fixCash:
                    result.append('\n$$\n')

                envs.append(expr.begin)
                result.append(expr.begin)
                process_latex_nodes(stuff, result, envs)
                result.append(expr.end)
                envs.pop()

                if fixCash:
                    result.append('\n$$\n\n')
            elif expr.begin == '\\begin{itemize}':
                envs.append(expr.begin)
                result.append('<ul markdown="1">\n')
                for item in stuff.contents:
                    result.append('<li markdown="1">')
                    process_latex_nodes(item, result, envs)
                    result.append('</li>\n')
                result.append('\n</ul>\n')
                envs.pop()
            elif expr.begin == '\\begin{enumerate}':
                envs.append(expr.begin)
                result.append('<ol markdown="1">\n')
                for item in stuff.contents:
                    result.append('<li markdown="1">')
                    process_latex_nodes(item, result, envs)
                    result.append('</li>\n')
                result.append('\n</ol>\n')
                envs.pop()
            else:
                result.append(str(stuff))
        else:
            raise RuntimeError('unknown node detected')

soup = TexSoup(data)
result = []
envs = []
process_latex_nodes(soup.document, result, envs)

with open('output.md', 'w') as outfile:
    outfile.write(''.join(result))
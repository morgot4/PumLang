import lang_files.syntaxis_analysis as syntaxis_analysis
import lang_files.lexical_analysis as lexical_analysis
import lang_files.evaluate as evaluate
import sys

try:
    params = []
    for i in sys.argv:
        params.append(i)
    lexems = lexical_analysis.lexical_analysis('test/5/main_test.plg')
    parser = syntaxis_analysis.Parser(lexems=lexems)
    parser.P()
    prn = evaluate.PrnEvaluate(parser.prn, parser.len_code)
    prn.evaluate()
except Exception as e:
    print(e.args)

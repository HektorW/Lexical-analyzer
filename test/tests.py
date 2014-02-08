import imp, sys

# token_definitions = imp.load_source('token_definitions', '../token_definitions.py')
Lexer = imp.load_source('Lexer', '../lexer.py').Lexer



json_tokens_file = 'tokens.json'


lex = Lexer(json_tokens_file)
lex.readJson()
lex.compile()





def testFailed(str):
  print('Test failed, ' + str)
  sys.exit()

def equals(result, expected):
  # assert(result == expected)
  if result != expected:
    testFailed('{} is not equal to {}'.format(result, expected))

def notequals(result, expected):
  # assert(result != expected)
  if result == expected:
    testFailed('{} should not equal {}'.format(result, expected))

def testNumbers():
  # test type
  equals(lex.getTokenType('1'), 'NUMBER')
  notequals(lex.getTokenType('a'), 'NUMBER')
  equals(lex.getTokenType('12312'), 'NUMBER')
  equals(lex.getTokenType('9128385123'), 'NUMBER')
  equals(lex.getTokenType('1.0'), 'NUMBER')
  equals(lex.getTokenType('1.'), 'NUMBER')
  equals(lex.getTokenType('.1'), 'NUMBER')
  equals(lex.getTokenType('1.1'), 'NUMBER')
  notequals(lex.getTokenType('NUMBER'), 'NUMBER')
  # notequals(lex.getTokenType('1.1.'), 'NUMBER')
  # notequals(lex.getTokenType('1.1.1'), 'NUMBER')

  # test value
  equals(lex.getTokenValue('1'), '1')
  equals(lex.getTokenValue('1.0'), '1.0')
  equals(lex.getTokenValue('1.'), '1.')
  equals(lex.getTokenValue('.1'), '.1')
  equals(lex.getTokenValue('12345.0123'), '12345.0123')
  equals(lex.getTokenValue('12345.0123'), '12345.0123')

  print('# Number tests passed')

def testStrings():
  equals(lex.getTokenType('"hello"'), 'STRING')
  equals(lex.getTokenType('"hello there walla"'), 'STRING')
  equals(lex.getTokenType('"1"'), 'STRING')
  notequals(lex.getTokenType('"1"'), 'NUMBER')

  print('# String tests passed')

# Run tests

testNumbers()
testStrings()
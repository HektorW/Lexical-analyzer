import imp, sys

# token_definitions = imp.load_source('token_definitions', '../token_definitions.py')
Lexer = imp.load_source('Lexer', '../lexer.py').Lexer



json_tokens_file = 'tokens.json'


lex = Lexer(json_tokens_file)
lex.readJson()
lex.compile()




# Testing framework, to be exchanged with something more robust
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




# Numbers
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

  # how is this handled? in more specific javascript logic
  # should you be able to specify rules between tokens?
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


# Strings
def testStrings():
  equals(lex.getTokenType('"hello"'), 'STRING')
  equals(lex.getTokenType('"hello there walla"'), 'STRING')
  equals(lex.getTokenType('"1"'), 'STRING')
  equals(lex.getTokenType('\'1\''), 'STRING')
  notequals(lex.getTokenType('"1"'), 'NUMBER')

  equals(lex.getTokenValue('"world"'), '"world"')
  equals(lex.getTokenValue('"one + 342.03 equals(=) somehting"'), '"one + 342.03 equals(=) somehting"')

  print('# String tests passed')


# Name
def testName():
  equals(lex.getTokenType('a'), 'NAME')
  equals(lex.getTokenType('albert'), 'NAME')
  equals(lex.getTokenType('foo'), 'NAME')
  equals(lex.getTokenType('foo_'), 'NAME')
  equals(lex.getTokenType('foo_1'), 'NAME')
  equals(lex.getTokenType('$'), 'NAME')
  equals(lex.getTokenType('_'), 'NAME')
  equals(lex.getTokenType('_$__$_asdafa99123_'), 'NAME')

  notequals(lex.getTokenType('_foo_1'), 'NAME') # should throw a error

  print('# Name tests passed')


# Run tests
testNumbers()
testStrings()
testName()
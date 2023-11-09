# Generated from Python.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,3,1,3,1,3,5,3,52,8,3,10,3,12,3,55,
        9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,68,8,5,1,6,4,
        6,71,8,6,11,6,12,6,72,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,3,9,86,8,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,94,8,10,10,10,12,
        10,97,9,10,1,10,1,10,3,10,101,8,10,1,10,0,1,6,11,0,2,4,6,8,10,12,
        14,16,18,20,0,3,1,0,1,4,1,0,5,9,1,0,18,21,107,0,25,1,0,0,0,2,32,
        1,0,0,0,4,34,1,0,0,0,6,46,1,0,0,0,8,56,1,0,0,0,10,67,1,0,0,0,12,
        70,1,0,0,0,14,74,1,0,0,0,16,78,1,0,0,0,18,85,1,0,0,0,20,100,1,0,
        0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,
        1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,
        33,3,8,4,0,31,33,3,4,2,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,
        0,34,35,3,12,6,0,35,38,7,0,0,0,36,39,3,12,6,0,37,39,3,6,3,0,38,36,
        1,0,0,0,38,37,1,0,0,0,39,5,1,0,0,0,40,41,6,3,-1,0,41,47,3,12,6,0,
        42,43,5,10,0,0,43,44,3,6,3,0,44,45,5,11,0,0,45,47,1,0,0,0,46,40,
        1,0,0,0,46,42,1,0,0,0,47,53,1,0,0,0,48,49,10,3,0,0,49,50,7,1,0,0,
        50,52,3,6,3,4,51,48,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,
        0,0,0,54,7,1,0,0,0,55,53,1,0,0,0,56,57,3,12,6,0,57,58,5,12,0,0,58,
        59,3,10,5,0,59,9,1,0,0,0,60,68,3,6,3,0,61,68,5,22,0,0,62,68,5,23,
        0,0,63,68,3,14,7,0,64,68,3,16,8,0,65,68,3,20,10,0,66,68,3,12,6,0,
        67,60,1,0,0,0,67,61,1,0,0,0,67,62,1,0,0,0,67,63,1,0,0,0,67,64,1,
        0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,11,1,0,0,0,69,71,7,2,0,0,70,
        69,1,0,0,0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,13,1,0,0,
        0,74,75,5,13,0,0,75,76,3,12,6,0,76,77,5,13,0,0,77,15,1,0,0,0,78,
        79,5,14,0,0,79,80,3,12,6,0,80,81,5,14,0,0,81,17,1,0,0,0,82,86,3,
        14,7,0,83,86,3,16,8,0,84,86,3,12,6,0,85,82,1,0,0,0,85,83,1,0,0,0,
        85,84,1,0,0,0,86,19,1,0,0,0,87,88,5,15,0,0,88,101,5,16,0,0,89,90,
        5,15,0,0,90,95,3,18,9,0,91,92,5,17,0,0,92,94,3,18,9,0,93,91,1,0,
        0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,
        1,0,0,0,98,99,5,16,0,0,99,101,1,0,0,0,100,87,1,0,0,0,100,89,1,0,
        0,0,101,21,1,0,0,0,10,25,32,38,46,53,67,72,85,95,100
    ]

class PythonParser ( Parser ):

    grammarFileName = "Python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+='", "'-='", "'*='", "'/='", "'*'", 
                     "'/'", "'+'", "'-'", "'%'", "'('", "')'", "'='", "'\"'", 
                     "'''", "'['", "']'", "','", "<INVALID>", "<INVALID>", 
                     "'_'", "<INVALID>", "'True'", "'False'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "CAP", "LOW", "UND", "INT", 
                      "TRE", "FLE", "WS" ]

    RULE_file_input = 0
    RULE_assignment_operators = 1
    RULE_assignment_arithmetic = 2
    RULE_expression = 3
    RULE_equal = 4
    RULE_equal_operand = 5
    RULE_variable = 6
    RULE_string = 7
    RULE_charquotes = 8
    RULE_comp_value = 9
    RULE_listing = 10

    ruleNames =  [ "file_input", "assignment_operators", "assignment_arithmetic", 
                   "expression", "equal", "equal_operand", "variable", "string", 
                   "charquotes", "comp_value", "listing" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    CAP=18
    LOW=19
    UND=20
    INT=21
    TRE=22
    FLE=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonParser.EOF, 0)

        def assignment_operators(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.Assignment_operatorsContext)
            else:
                return self.getTypedRuleContext(PythonParser.Assignment_operatorsContext,i)


        def getRuleIndex(self):
            return PythonParser.RULE_file_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_input" ):
                listener.enterFile_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_input" ):
                listener.exitFile_input(self)




    def file_input(self):

        localctx = PythonParser.File_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0):
                self.state = 22
                self.assignment_operators()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(PythonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equal(self):
            return self.getTypedRuleContext(PythonParser.EqualContext,0)


        def assignment_arithmetic(self):
            return self.getTypedRuleContext(PythonParser.Assignment_arithmeticContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_assignment_operators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operators" ):
                listener.enterAssignment_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operators" ):
                listener.exitAssignment_operators(self)




    def assignment_operators(self):

        localctx = PythonParser.Assignment_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assignment_operators)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.equal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.assignment_arithmetic()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.VariableContext)
            else:
                return self.getTypedRuleContext(PythonParser.VariableContext,i)


        def expression(self):
            return self.getTypedRuleContext(PythonParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_assignment_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_arithmetic" ):
                listener.enterAssignment_arithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_arithmetic" ):
                listener.exitAssignment_arithmetic(self)




    def assignment_arithmetic(self):

        localctx = PythonParser.Assignment_arithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.variable()
            self.state = 35
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 36
                self.variable()
                pass

            elif la_ == 2:
                self.state = 37
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PythonParser.VariableContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PythonParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 21]:
                self.state = 41
                self.variable()
                pass
            elif token in [10]:
                self.state = 42
                self.match(PythonParser.T__9)
                self.state = 43
                self.expression(0)
                self.state = 44
                self.match(PythonParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 48
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 49
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 50
                    self.expression(4) 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EqualContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PythonParser.VariableContext,0)


        def equal_operand(self):
            return self.getTypedRuleContext(PythonParser.Equal_operandContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_equal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)




    def equal(self):

        localctx = PythonParser.EqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.variable()
            self.state = 57
            self.match(PythonParser.T__11)
            self.state = 58
            self.equal_operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equal_operandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PythonParser.ExpressionContext,0)


        def TRE(self):
            return self.getToken(PythonParser.TRE, 0)

        def FLE(self):
            return self.getToken(PythonParser.FLE, 0)

        def string(self):
            return self.getTypedRuleContext(PythonParser.StringContext,0)


        def charquotes(self):
            return self.getTypedRuleContext(PythonParser.CharquotesContext,0)


        def listing(self):
            return self.getTypedRuleContext(PythonParser.ListingContext,0)


        def variable(self):
            return self.getTypedRuleContext(PythonParser.VariableContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_equal_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual_operand" ):
                listener.enterEqual_operand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual_operand" ):
                listener.exitEqual_operand(self)




    def equal_operand(self):

        localctx = PythonParser.Equal_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_equal_operand)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(PythonParser.TRE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.match(PythonParser.FLE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.string()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.charquotes()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.listing()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 66
                self.variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAP(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.CAP)
            else:
                return self.getToken(PythonParser.CAP, i)

        def LOW(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.LOW)
            else:
                return self.getToken(PythonParser.LOW, i)

        def UND(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.UND)
            else:
                return self.getToken(PythonParser.UND, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.INT)
            else:
                return self.getToken(PythonParser.INT, i)

        def getRuleIndex(self):
            return PythonParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = PythonParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 69
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 72 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PythonParser.VariableContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = PythonParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(PythonParser.T__12)
            self.state = 75
            self.variable()
            self.state = 76
            self.match(PythonParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharquotesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PythonParser.VariableContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_charquotes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharquotes" ):
                listener.enterCharquotes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharquotes" ):
                listener.exitCharquotes(self)




    def charquotes(self):

        localctx = PythonParser.CharquotesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_charquotes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(PythonParser.T__13)
            self.state = 79
            self.variable()
            self.state = 80
            self.match(PythonParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(PythonParser.StringContext,0)


        def charquotes(self):
            return self.getTypedRuleContext(PythonParser.CharquotesContext,0)


        def variable(self):
            return self.getTypedRuleContext(PythonParser.VariableContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_comp_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_value" ):
                listener.enterComp_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_value" ):
                listener.exitComp_value(self)




    def comp_value(self):

        localctx = PythonParser.Comp_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comp_value)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.string()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.charquotes()
                pass
            elif token in [18, 19, 20, 21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.Comp_valueContext)
            else:
                return self.getTypedRuleContext(PythonParser.Comp_valueContext,i)


        def getRuleIndex(self):
            return PythonParser.RULE_listing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListing" ):
                listener.enterListing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListing" ):
                listener.exitListing(self)




    def listing(self):

        localctx = PythonParser.ListingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_listing)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(PythonParser.T__14)
                self.state = 88
                self.match(PythonParser.T__15)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(PythonParser.T__14)
                self.state = 90
                self.comp_value()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 91
                    self.match(PythonParser.T__16)
                    self.state = 92
                    self.comp_value()
                    self.state = 97
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 98
                self.match(PythonParser.T__15)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         





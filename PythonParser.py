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
        4,1,24,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,3,0,23,8,0,1,1,1,1,1,1,1,1,3,1,
        29,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,1,2,1,2,1,2,5,2,42,8,2,
        10,2,12,2,45,9,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        58,8,4,1,5,4,5,61,8,5,11,5,12,5,62,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,3,8,76,8,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,84,8,9,10,9,
        12,9,87,9,9,1,9,1,9,3,9,91,8,9,1,9,0,1,4,10,0,2,4,6,8,10,12,14,16,
        18,0,3,1,0,1,4,1,0,5,9,1,0,18,21,97,0,22,1,0,0,0,2,24,1,0,0,0,4,
        36,1,0,0,0,6,46,1,0,0,0,8,57,1,0,0,0,10,60,1,0,0,0,12,64,1,0,0,0,
        14,68,1,0,0,0,16,75,1,0,0,0,18,90,1,0,0,0,20,23,3,6,3,0,21,23,3,
        2,1,0,22,20,1,0,0,0,22,21,1,0,0,0,23,1,1,0,0,0,24,25,3,10,5,0,25,
        28,7,0,0,0,26,29,3,10,5,0,27,29,3,4,2,0,28,26,1,0,0,0,28,27,1,0,
        0,0,29,3,1,0,0,0,30,31,6,2,-1,0,31,37,3,10,5,0,32,33,5,10,0,0,33,
        34,3,4,2,0,34,35,5,11,0,0,35,37,1,0,0,0,36,30,1,0,0,0,36,32,1,0,
        0,0,37,43,1,0,0,0,38,39,10,3,0,0,39,40,7,1,0,0,40,42,3,4,2,4,41,
        38,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,5,1,0,0,
        0,45,43,1,0,0,0,46,47,3,10,5,0,47,48,5,12,0,0,48,49,3,8,4,0,49,7,
        1,0,0,0,50,58,3,4,2,0,51,58,5,22,0,0,52,58,5,23,0,0,53,58,3,12,6,
        0,54,58,3,14,7,0,55,58,3,18,9,0,56,58,3,10,5,0,57,50,1,0,0,0,57,
        51,1,0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,57,54,1,0,0,0,57,55,1,0,0,
        0,57,56,1,0,0,0,58,9,1,0,0,0,59,61,7,2,0,0,60,59,1,0,0,0,61,62,1,
        0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,11,1,0,0,0,64,65,5,13,0,0,65,
        66,3,10,5,0,66,67,5,13,0,0,67,13,1,0,0,0,68,69,5,14,0,0,69,70,3,
        10,5,0,70,71,5,14,0,0,71,15,1,0,0,0,72,76,3,12,6,0,73,76,3,14,7,
        0,74,76,3,10,5,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,17,
        1,0,0,0,77,78,5,15,0,0,78,91,5,16,0,0,79,80,5,15,0,0,80,85,3,16,
        8,0,81,82,5,17,0,0,82,84,3,16,8,0,83,81,1,0,0,0,84,87,1,0,0,0,85,
        83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,89,5,16,
        0,0,89,91,1,0,0,0,90,77,1,0,0,0,90,79,1,0,0,0,91,19,1,0,0,0,9,22,
        28,36,43,57,62,75,85,90
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

    RULE_assignment_operators = 0
    RULE_assignment_arithmetic = 1
    RULE_expression = 2
    RULE_equal = 3
    RULE_equal_operand = 4
    RULE_variable = 5
    RULE_string = 6
    RULE_charquotes = 7
    RULE_comp_value = 8
    RULE_listing = 9

    ruleNames =  [ "assignment_operators", "assignment_arithmetic", "expression", 
                   "equal", "equal_operand", "variable", "string", "charquotes", 
                   "comp_value", "listing" ]

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_operators" ):
                return visitor.visitAssignment_operators(self)
            else:
                return visitor.visitChildren(self)




    def assignment_operators(self):

        localctx = PythonParser.Assignment_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_assignment_operators)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.equal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_arithmetic" ):
                return visitor.visitAssignment_arithmetic(self)
            else:
                return visitor.visitChildren(self)




    def assignment_arithmetic(self):

        localctx = PythonParser.Assignment_arithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assignment_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.variable()
            self.state = 25
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 26
                self.variable()
                pass

            elif la_ == 2:
                self.state = 27
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 21]:
                self.state = 31
                self.variable()
                pass
            elif token in [10]:
                self.state = 32
                self.match(PythonParser.T__9)
                self.state = 33
                self.expression(0)
                self.state = 34
                self.match(PythonParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 38
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 39
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 40
                    self.expression(4) 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)




    def equal(self):

        localctx = PythonParser.EqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.variable()
            self.state = 47
            self.match(PythonParser.T__11)
            self.state = 48
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual_operand" ):
                return visitor.visitEqual_operand(self)
            else:
                return visitor.visitChildren(self)




    def equal_operand(self):

        localctx = PythonParser.Equal_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_equal_operand)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(PythonParser.TRE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(PythonParser.FLE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.string()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.charquotes()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.listing()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = PythonParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 59
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 62 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = PythonParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(PythonParser.T__12)
            self.state = 65
            self.variable()
            self.state = 66
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharquotes" ):
                return visitor.visitCharquotes(self)
            else:
                return visitor.visitChildren(self)




    def charquotes(self):

        localctx = PythonParser.CharquotesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_charquotes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PythonParser.T__13)
            self.state = 69
            self.variable()
            self.state = 70
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_value" ):
                return visitor.visitComp_value(self)
            else:
                return visitor.visitChildren(self)




    def comp_value(self):

        localctx = PythonParser.Comp_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comp_value)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.string()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.charquotes()
                pass
            elif token in [18, 19, 20, 21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListing" ):
                return visitor.visitListing(self)
            else:
                return visitor.visitChildren(self)




    def listing(self):

        localctx = PythonParser.ListingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listing)
        self._la = 0 # Token type
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(PythonParser.T__14)
                self.state = 78
                self.match(PythonParser.T__15)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(PythonParser.T__14)
                self.state = 80
                self.comp_value()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 81
                    self.match(PythonParser.T__16)
                    self.state = 82
                    self.comp_value()
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 88
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
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         





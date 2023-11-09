# Generated from Python.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#file_input.
    def enterFile_input(self, ctx:PythonParser.File_inputContext):
        pass

    # Exit a parse tree produced by PythonParser#file_input.
    def exitFile_input(self, ctx:PythonParser.File_inputContext):
        pass


    # Enter a parse tree produced by PythonParser#assignment_operators.
    def enterAssignment_operators(self, ctx:PythonParser.Assignment_operatorsContext):
        pass

    # Exit a parse tree produced by PythonParser#assignment_operators.
    def exitAssignment_operators(self, ctx:PythonParser.Assignment_operatorsContext):
        pass


    # Enter a parse tree produced by PythonParser#assignment_arithmetic.
    def enterAssignment_arithmetic(self, ctx:PythonParser.Assignment_arithmeticContext):
        pass

    # Exit a parse tree produced by PythonParser#assignment_arithmetic.
    def exitAssignment_arithmetic(self, ctx:PythonParser.Assignment_arithmeticContext):
        pass


    # Enter a parse tree produced by PythonParser#expression.
    def enterExpression(self, ctx:PythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonParser#expression.
    def exitExpression(self, ctx:PythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonParser#equal.
    def enterEqual(self, ctx:PythonParser.EqualContext):
        pass

    # Exit a parse tree produced by PythonParser#equal.
    def exitEqual(self, ctx:PythonParser.EqualContext):
        pass


    # Enter a parse tree produced by PythonParser#equal_operand.
    def enterEqual_operand(self, ctx:PythonParser.Equal_operandContext):
        pass

    # Exit a parse tree produced by PythonParser#equal_operand.
    def exitEqual_operand(self, ctx:PythonParser.Equal_operandContext):
        pass


    # Enter a parse tree produced by PythonParser#variable.
    def enterVariable(self, ctx:PythonParser.VariableContext):
        pass

    # Exit a parse tree produced by PythonParser#variable.
    def exitVariable(self, ctx:PythonParser.VariableContext):
        pass


    # Enter a parse tree produced by PythonParser#string.
    def enterString(self, ctx:PythonParser.StringContext):
        pass

    # Exit a parse tree produced by PythonParser#string.
    def exitString(self, ctx:PythonParser.StringContext):
        pass


    # Enter a parse tree produced by PythonParser#charquotes.
    def enterCharquotes(self, ctx:PythonParser.CharquotesContext):
        pass

    # Exit a parse tree produced by PythonParser#charquotes.
    def exitCharquotes(self, ctx:PythonParser.CharquotesContext):
        pass


    # Enter a parse tree produced by PythonParser#comp_value.
    def enterComp_value(self, ctx:PythonParser.Comp_valueContext):
        pass

    # Exit a parse tree produced by PythonParser#comp_value.
    def exitComp_value(self, ctx:PythonParser.Comp_valueContext):
        pass


    # Enter a parse tree produced by PythonParser#listing.
    def enterListing(self, ctx:PythonParser.ListingContext):
        pass

    # Exit a parse tree produced by PythonParser#listing.
    def exitListing(self, ctx:PythonParser.ListingContext):
        pass



del PythonParser
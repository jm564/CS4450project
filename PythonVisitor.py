# Generated from Python.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#file_input.
    def visitFile_input(self, ctx:PythonParser.File_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#assignment_operators.
    def visitAssignment_operators(self, ctx:PythonParser.Assignment_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#assignment_arithmetic.
    def visitAssignment_arithmetic(self, ctx:PythonParser.Assignment_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expression.
    def visitExpression(self, ctx:PythonParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#equal.
    def visitEqual(self, ctx:PythonParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#equal_operand.
    def visitEqual_operand(self, ctx:PythonParser.Equal_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#variable.
    def visitVariable(self, ctx:PythonParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#string.
    def visitString(self, ctx:PythonParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#charquotes.
    def visitCharquotes(self, ctx:PythonParser.CharquotesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#comp_value.
    def visitComp_value(self, ctx:PythonParser.Comp_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#listing.
    def visitListing(self, ctx:PythonParser.ListingContext):
        return self.visitChildren(ctx)



del PythonParser
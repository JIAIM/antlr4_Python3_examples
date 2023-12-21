# Generated from D:/python KPI/antlr4_Python3_examples/Tovid.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TovidParser import TovidParser
else:
    from TovidParser import TovidParser

# This class defines a complete listener for a parse tree produced by TovidParser.
class TovidListener(ParseTreeListener):

    # Enter a parse tree produced by TovidParser#program.
    def enterProgram(self, ctx:TovidParser.ProgramContext):
        pass

    # Exit a parse tree produced by TovidParser#program.
    def exitProgram(self, ctx:TovidParser.ProgramContext):
        pass


    # Enter a parse tree produced by TovidParser#statement.
    def enterStatement(self, ctx:TovidParser.StatementContext):
        pass

    # Exit a parse tree produced by TovidParser#statement.
    def exitStatement(self, ctx:TovidParser.StatementContext):
        pass


    # Enter a parse tree produced by TovidParser#funcDeclaration.
    def enterFuncDeclaration(self, ctx:TovidParser.FuncDeclarationContext):
        pass

    # Exit a parse tree produced by TovidParser#funcDeclaration.
    def exitFuncDeclaration(self, ctx:TovidParser.FuncDeclarationContext):
        pass


    # Enter a parse tree produced by TovidParser#parameters.
    def enterParameters(self, ctx:TovidParser.ParametersContext):
        pass

    # Exit a parse tree produced by TovidParser#parameters.
    def exitParameters(self, ctx:TovidParser.ParametersContext):
        pass


    # Enter a parse tree produced by TovidParser#parameter.
    def enterParameter(self, ctx:TovidParser.ParameterContext):
        pass

    # Exit a parse tree produced by TovidParser#parameter.
    def exitParameter(self, ctx:TovidParser.ParameterContext):
        pass


    # Enter a parse tree produced by TovidParser#type.
    def enterType(self, ctx:TovidParser.TypeContext):
        pass

    # Exit a parse tree produced by TovidParser#type.
    def exitType(self, ctx:TovidParser.TypeContext):
        pass


    # Enter a parse tree produced by TovidParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:TovidParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by TovidParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:TovidParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by TovidParser#assignment.
    def enterAssignment(self, ctx:TovidParser.AssignmentContext):
        pass

    # Exit a parse tree produced by TovidParser#assignment.
    def exitAssignment(self, ctx:TovidParser.AssignmentContext):
        pass


    # Enter a parse tree produced by TovidParser#printStatement.
    def enterPrintStatement(self, ctx:TovidParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by TovidParser#printStatement.
    def exitPrintStatement(self, ctx:TovidParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by TovidParser#scanStatement.
    def enterScanStatement(self, ctx:TovidParser.ScanStatementContext):
        pass

    # Exit a parse tree produced by TovidParser#scanStatement.
    def exitScanStatement(self, ctx:TovidParser.ScanStatementContext):
        pass


    # Enter a parse tree produced by TovidParser#ifStatement.
    def enterIfStatement(self, ctx:TovidParser.IfStatementContext):
        pass

    # Exit a parse tree produced by TovidParser#ifStatement.
    def exitIfStatement(self, ctx:TovidParser.IfStatementContext):
        pass


    # Enter a parse tree produced by TovidParser#forStatement.
    def enterForStatement(self, ctx:TovidParser.ForStatementContext):
        pass

    # Exit a parse tree produced by TovidParser#forStatement.
    def exitForStatement(self, ctx:TovidParser.ForStatementContext):
        pass


    # Enter a parse tree produced by TovidParser#returnStatement.
    def enterReturnStatement(self, ctx:TovidParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by TovidParser#returnStatement.
    def exitReturnStatement(self, ctx:TovidParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by TovidParser#block.
    def enterBlock(self, ctx:TovidParser.BlockContext):
        pass

    # Exit a parse tree produced by TovidParser#block.
    def exitBlock(self, ctx:TovidParser.BlockContext):
        pass


    # Enter a parse tree produced by TovidParser#expression.
    def enterExpression(self, ctx:TovidParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TovidParser#expression.
    def exitExpression(self, ctx:TovidParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TovidParser#assignExpression.
    def enterAssignExpression(self, ctx:TovidParser.AssignExpressionContext):
        pass

    # Exit a parse tree produced by TovidParser#assignExpression.
    def exitAssignExpression(self, ctx:TovidParser.AssignExpressionContext):
        pass


    # Enter a parse tree produced by TovidParser#arithmExpression.
    def enterArithmExpression(self, ctx:TovidParser.ArithmExpressionContext):
        pass

    # Exit a parse tree produced by TovidParser#arithmExpression.
    def exitArithmExpression(self, ctx:TovidParser.ArithmExpressionContext):
        pass


    # Enter a parse tree produced by TovidParser#term.
    def enterTerm(self, ctx:TovidParser.TermContext):
        pass

    # Exit a parse tree produced by TovidParser#term.
    def exitTerm(self, ctx:TovidParser.TermContext):
        pass


    # Enter a parse tree produced by TovidParser#factor.
    def enterFactor(self, ctx:TovidParser.FactorContext):
        pass

    # Exit a parse tree produced by TovidParser#factor.
    def exitFactor(self, ctx:TovidParser.FactorContext):
        pass


    # Enter a parse tree produced by TovidParser#booleanExpression.
    def enterBooleanExpression(self, ctx:TovidParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by TovidParser#booleanExpression.
    def exitBooleanExpression(self, ctx:TovidParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by TovidParser#addOp.
    def enterAddOp(self, ctx:TovidParser.AddOpContext):
        pass

    # Exit a parse tree produced by TovidParser#addOp.
    def exitAddOp(self, ctx:TovidParser.AddOpContext):
        pass


    # Enter a parse tree produced by TovidParser#multOp.
    def enterMultOp(self, ctx:TovidParser.MultOpContext):
        pass

    # Exit a parse tree produced by TovidParser#multOp.
    def exitMultOp(self, ctx:TovidParser.MultOpContext):
        pass


    # Enter a parse tree produced by TovidParser#powOp.
    def enterPowOp(self, ctx:TovidParser.PowOpContext):
        pass

    # Exit a parse tree produced by TovidParser#powOp.
    def exitPowOp(self, ctx:TovidParser.PowOpContext):
        pass


    # Enter a parse tree produced by TovidParser#compareOp.
    def enterCompareOp(self, ctx:TovidParser.CompareOpContext):
        pass

    # Exit a parse tree produced by TovidParser#compareOp.
    def exitCompareOp(self, ctx:TovidParser.CompareOpContext):
        pass


    # Enter a parse tree produced by TovidParser#logicOp.
    def enterLogicOp(self, ctx:TovidParser.LogicOpContext):
        pass

    # Exit a parse tree produced by TovidParser#logicOp.
    def exitLogicOp(self, ctx:TovidParser.LogicOpContext):
        pass


    # Enter a parse tree produced by TovidParser#unaryOp.
    def enterUnaryOp(self, ctx:TovidParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by TovidParser#unaryOp.
    def exitUnaryOp(self, ctx:TovidParser.UnaryOpContext):
        pass



del TovidParser
# Generated from D:/python KPI/antlr4_Python3_examples/Tovid.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TovidParser import TovidParser
else:
    from TovidParser import TovidParser

# This class defines a complete generic visitor for a parse tree produced by TovidParser.

class TovidVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TovidParser#program.
    def visitProgram(self, ctx:TovidParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#statement.
    def visitStatement(self, ctx:TovidParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#funcDeclaration.
    def visitFuncDeclaration(self, ctx:TovidParser.FuncDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#parameters.
    def visitParameters(self, ctx:TovidParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#parameter.
    def visitParameter(self, ctx:TovidParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#type.
    def visitType(self, ctx:TovidParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:TovidParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#assignment.
    def visitAssignment(self, ctx:TovidParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#printStatement.
    def visitPrintStatement(self, ctx:TovidParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#scanStatement.
    def visitScanStatement(self, ctx:TovidParser.ScanStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#ifStatement.
    def visitIfStatement(self, ctx:TovidParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#forStatement.
    def visitForStatement(self, ctx:TovidParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#returnStatement.
    def visitReturnStatement(self, ctx:TovidParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#block.
    def visitBlock(self, ctx:TovidParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#expression.
    def visitExpression(self, ctx:TovidParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#assignExpression.
    def visitAssignExpression(self, ctx:TovidParser.AssignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#arithmExpression.
    def visitArithmExpression(self, ctx:TovidParser.ArithmExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#term.
    def visitTerm(self, ctx:TovidParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#factor.
    def visitFactor(self, ctx:TovidParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#booleanExpression.
    def visitBooleanExpression(self, ctx:TovidParser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#addOp.
    def visitAddOp(self, ctx:TovidParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#multOp.
    def visitMultOp(self, ctx:TovidParser.MultOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#powOp.
    def visitPowOp(self, ctx:TovidParser.PowOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#compareOp.
    def visitCompareOp(self, ctx:TovidParser.CompareOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#logicOp.
    def visitLogicOp(self, ctx:TovidParser.LogicOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TovidParser#unaryOp.
    def visitUnaryOp(self, ctx:TovidParser.UnaryOpContext):
        return self.visitChildren(ctx)



del TovidParser
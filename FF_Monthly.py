import FF_SalesInstall
import FF_GLDetail
import FF_Employees
import FF_OpCode


def monthlyrun():
    FF_Employees.employees()
    FF_OpCode.opcode()


monthlyrun()

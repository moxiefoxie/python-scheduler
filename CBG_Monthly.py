import FF_SalesInstall
import FF_GLDetail
import CBG_Employees
import CBG_OpCode


def monthlyrun():
    CBG_Employees.employees()
    CBG_OpCode.opcode()


monthlyrun()

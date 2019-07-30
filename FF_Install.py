import FF_SalesInstall
import FF_GLDetail
import FF_Employees
import FF_OpCode



def installrun():
    FF_SalesInstall.salesinstall()
    FF_GLDetail.gldetail()
    FF_Employees.employees()
    FF_OpCode.opcode()



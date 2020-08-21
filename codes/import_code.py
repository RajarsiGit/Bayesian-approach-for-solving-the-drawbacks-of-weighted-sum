import xlrd
from matrix import Matrix

class Import_Code(object):
#class for importing distance, time and availability matrices from excel file
    
    def create_matrices(self):
        #function to create matrices
        
        wb = xlrd.open_workbook('Matrices_SET2.xlsx')
        sheet1 = wb.sheet_by_index(0) 
        sheet2 = wb.sheet_by_index(1)
        sheet3 = wb.sheet_by_index(2)

        matrices = Matrix([[0 for i in xrange(sheet1.ncols)] for i in xrange(sheet1.nrows)], [[0 for i in xrange(sheet2.ncols)] for i in xrange(sheet2.nrows)], [0 for i in xrange(sheet3.ncols)])

        for i in range(sheet1.nrows):
            for j in range(sheet1.ncols):
                matrices.time[i][j] = sheet1.cell_value(i,j)
        
        for i in range(sheet2.nrows):
            for j in range(sheet2.ncols):
                matrices.distance[i][j] = sheet2.cell_value(i,j)
        
        for i in range(sheet3.ncols):
            matrices.availability[i] = sheet3.cell_value(0,i)
            
        return matrices
    
if __name__ == "__main__":
    imp = Import_Code()
    matrices = imp.create_matrices()
    print matrices.time
    print matrices.distance
    print matrices.availability
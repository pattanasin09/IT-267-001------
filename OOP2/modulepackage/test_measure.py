"""import measure_convert as measure

if __name__ == '__main__':
    inch = float(input('กรอกหน่วยนิ้วที่ต้องการจะแปลง : '))
    print (f'{inch} นิ้ว = {measure.inch_to_cm(inch):.2f} เซนติเมตร')

    cm = float(input('กรอกหน่วยเซนที่ต้องการจะแปลง : '))
    print(f'{cm} เซนติเมตร = {measure.cm_to_inch(cm):.2f} นิ้ว')"""

from measure_convert import  inch_to_cm , cm_to_inch

if __name__ == '__main__':
    print(inch_to_cm(12.5))
    print(cm_to_inch(100)
    )

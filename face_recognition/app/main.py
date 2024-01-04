# import streamlit as st
# import cv2

# from datetime import datetime
# import time



# import streamlit as st
# import pandas as pd
# from datetime import datetime


# file_path = r'D:\WorkSpace\KhaiPhaDuLieu\classifier\face_recognition\app\danhsachsinhvien\danhsachsinhvien.csv'
# lop_hoc_phan = "Khai phá dữ liệu - Nhóm 1"
# ma_lop_hoc_phan = "2023-2024.1.TIN4103.001"
# giang_vien = "Nguyễn Ngọc Thủy (1990)"


# def save_to_csv(df):
#     # Chọn vị trí lưu file CSV
#     file_path = st.file_uploader("Chọn nơi lưu file CSV", type=["csv"])

#     # Lưu DataFrame vào file CSV nếu người dùng đã chọn vị trí lưu
#     if file_path:
#         df.to_csv(file_path, index=False)
#         st.success("DataFrame đã được lưu vào file CSV thành công!")

# def view_dataframe(df, state, title):
#     # Tạo một nút để xem hoặc ẩn DataFrame
#     if st.button(title):
#         state.show_df = not state.show_df

#     # Hiển thị DataFrame nếu biến trạng thái là True
#     if state.show_df:
#         st.dataframe(df)

# # def view_dataframe(df, state, df_name, title):
# #     # Tạo một nút để xem hoặc ẩn DataFrame
# #     if st.button(f"Xem/Ẩn {df_name} DataFrame"):
# #         state[df_name] = not state[df_name]

# #     # Hiển thị DataFrame nếu biến trạng thái là True
# #     if state[df_name]:
# #         st.dataframe(df)


# def ThongKe(filePath, lopHocPhan,maLopHocPhan, giangVien):
#     # Đọc dữ liệu từ file CSV
#     # st.title("Trang Chính")
#     file_path = filePath
#     # file_path = "data.csv"
#     data = pd.read_csv(file_path)

#     # Thông tin về lớp học phần
#     lop_hoc_phan = lopHocPhan
#     ma_lop_hoc_phan = maLopHocPhan
#     giang_vien = giangVien

#     # Layout của ứng dụng
#     header_col, info_col = st.columns([1, 2])

#     # Hiển thị nút "Home"
#     home_button = st.button("Home")

#     # Xử lý sự kiện khi nút "Home" được nhấn
#     if home_button:
#         home_screen(title='Thông tin lớp học phần', monhoc='Khai Phá Dữ Liệu', giangvien='Nguyễn Ngọc Thủy (1990)', thoigianbatdau= '13:00:00', thoigianketthuc= '16:00:00')

#     else:
#         # Hiển thị tiêu đề
#         with header_col:
#             st.title("Thông Tin Lớp Học Phần")

#         # Hiển thị thông tin
#         with info_col:
#             st.subheader("Tên Lớp Học Phần:")
#             st.write(lop_hoc_phan)

#             st.subheader("Mã Lớp Học Phần:")
#             st.write(ma_lop_hoc_phan)

#             st.subheader("Giảng Viên:")
#             st.write(giang_vien)
        


#         # Hiển thị dữ liệu bảng
#         if 'show_df' not in st.session_state:
#             st.session_state.show_df = False
#         view_dataframe(data.iloc[:, :7], st.session_state, "Danh sách sinh viên của lớp học phần")
#         # view_dataframe(data, show_df,"Danh sách sinh viên của lớp học phần" )
    

#         # Chuyển đổi cột 'Ngày sinh' sang định dạng datetime
#         data['Ngày sinh'] = pd.to_datetime(data['Ngày sinh'], format='%d/%m/%Y')

#         # Thống kê số lượng sinh viên nghỉ và đi học trong ngày
#         ngay_hien_tai = datetime.now().date()
        


#         sinh_vien_nghi_hoc = data[data['Ngày sinh'].dt.date == ngay_hien_tai]
#         sinh_vien_di_hoc = data[data['Ngày sinh'].dt.date != ngay_hien_tai]

#         # Hiển thị thống kê
#         st.subheader(f"Thống Kê Sinh Viên Ngày {ngay_hien_tai.strftime('%d/%m/%Y')}")
#         st.write(f"Số lượng sinh viên nghỉ học: {len(sinh_vien_nghi_hoc)}")
#         st.write(f"Số lượng sinh viên đi học: {len(sinh_vien_di_hoc)}")

#         if str(ngay_hien_tai) != data.iloc[0, -1]:
#             data[ngay_hien_tai] = 999
#             # data.to_csv('data.csv', index=False)
#         st.dataframe(data)

        


#         # Hiển thị danh sách sinh viên nghỉ học
#         if st.button("Danh Sách Sinh Viên Nghỉ Học"):
#             st.dataframe(sinh_vien_nghi_hoc)
#         # if 'show_df1' not in st.session_state:
#         #     st.session_state.show_df1 = False
#         # view_dataframe(sinh_vien_nghi_hoc, st.session_state, "Danh Sách Sinh Viên Nghỉ Học")
    

#         # Hiển thị danh sách sinh viên đi học
#         if st.button("Danh Sách Sinh Viên Đi Học"):
#             st.dataframe(sinh_vien_di_hoc)







# def onclick_btn1():
#     print('btn1')
# def onclick_btn2():
#     st.experimental_set_query_params(home=True)
#     ThongKe(file_path, lop_hoc_phan, ma_lop_hoc_phan, giang_vien)
#     return

# def home_screen(title, monhoc, giangvien, thoigianbatdau, thoigianketthuc):
#     # st.title("Trang Chính")
#     st.title(title)
#     col1, col2  = st.columns(2)

#     _, current_time_col = st.columns(2)

  
#     label1 = col1.empty()
#     label2 = col2.empty()

#     time_label = current_time_col.empty()

   

#     # label3 = col3.empty()
#     # label4 = col4.empty()

#     st.text("Thời gian bắt đầu: " + thoigianbatdau)
#     st.text('Thời gian kết thúc: ' + thoigianketthuc)

#     colbtn1, colbtn2  = st.columns(2)
#     labelbtn1 = colbtn1.empty()
#     labelbtn2 = colbtn2.empty()
#     btn1 = st.button('Điểm danh vào lớp', key='diemdanh',on_click=onclick_btn1)
#     btn2 = st.button('Kết quả điểm danh', key='thongke', on_click= onclick_btn2)

#     while True:
#         # btn1 = False
#         # btn2 = False
#         # Lấy thời gian hiện tại
#         current_time = datetime.now()

#         # Định dạng thời gian theo yêu cầu: HH:mm:ss
#         formatted_time = current_time.strftime("%H:%M:%S")

#         # Cập nhật nội dung của các phần tử
#         label1.text('Môn học: ' + monhoc)
#         label2.text('Giảng viên: ' + giangvien)

#         # Xóa toàn bộ nội dung của cửa sổ trước khi in thời gian mới
#         time_label.text('Thời gian hiện tại: ' + formatted_time)

#         # Tạm dừng 1 giây trước khi cập nhật lại thời gian
#         time.sleep(1)




# home_screen(title='Thông tin lớp học phần', monhoc='Khai Phá Dữ Liệu', giangvien='Nguyễn Ngọc Thủy (1990)', thoigianbatdau= '13:00:00', thoigianketthuc= '16:00:00')



# # ThongKe(file_path, lop_hoc_phan, ma_lop_hoc_phan, giang_vien)
# # Kết thúc khi nhấn nút dừng
# # cap.release()
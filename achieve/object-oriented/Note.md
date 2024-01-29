## Static method
```
class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def static_method():
        # Không có tham số self ở đây
        print("This is a static method.")

# Gọi static method không cần tạo đối tượng của lớp
MyClass.static_method()

```

## repr method and eval method
```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

# Tạo một đối tượng Point
p = Point(10, 20)

# Sử dụng phương thức repr() để lấy chuỗi biểu diễn của đối tượng
repr_str = repr(p)
print(repr_str)  # Output: "Point(x=10, y=20)"

# Sử dụng hàm eval() để tái tạo đối tượng từ chuỗi biểu diễn
new_p = eval(repr_str)
print(new_p)  # Output: Point(x=10, y=20)

```

## Multiple Inheritance
- Doi khi, ban co the can them mot hanh vi nhat dinh vao nhieu lop khong lien quan.

import math

class FlexibleTriangle:
    def __init__(self, AB=60, BC=60, CA=60, A=1, B=1, C=1):
        self.AB = AB
        self.BC = BC
        self.CA = CA
        self.A = A
        self.B = B
        self.C = C

    def modify_angle(self, angle, degrees):
        if angle not in {'AB', 'BC', 'CA'}:
            raise ValueError("Invalid angle. Use 'AB', 'BC', or 'CA'.")

        if angle == 'AB':
            self.AB += degrees
        elif angle == 'BC':
            self.BC += degrees
        elif angle == 'CA':
            self.CA += degrees

        # Check if any angle is outside the valid range
        if any(angle <= 0 or angle >= 180 for angle in (self.AB, self.BC, self.CA)):
            raise ValueError("Invalid angle. Angle must be in the range (0, 180).")

        # Recalculate sides
        self.C = math.sqrt(self.A ** 2 + self.B ** 2 - 2 * self.A * self.B * math.cos(math.radians(self.AB)))
        self.A = math.sqrt(self.B ** 2 + self.C ** 2 - 2 * self.B * self.C * math.cos(math.radians(self.BC)))
        self.B = math.sqrt(self.C ** 2 + self.A ** 2 - 2 * self.C * self.A * math.cos(math.radians(self.CA)))

    def modify_side(self, side, meters):
        if side not in {'A', 'B', 'C'}:
            raise ValueError("Invalid side. Use 'A', 'B', or 'C'.")

        if side == 'A':
            self.A += meters
        elif side == 'B':
            self.B += meters
        elif side == 'C':
            self.C += meters

        # Check if the sum of unmodified sides is less than or equal to the changed side
        if (self.A + self.B <= self.C) or (self.B + self.C <= self.A) or (self.C + self.A <= self.B):
            raise ValueError(
                "Invalid side modification. Sum of unmodified sides must be greater than the changed side.")

        # Check if the side is less than or equal to 0
        if any(side <= 0 for side in (self.A, self.B, self.C)):
            raise ValueError("Invalid side. Side must be greater than 0.")

        # Recalculate angles
        self.AB = math.degrees(math.acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C)))
        self.BC = math.degrees(math.acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A)))
        self.CA = math.degrees(math.acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B)))


# Example usage:
triangle = FlexibleTriangle()

print("Initial angles and sides:")
print("AB:", triangle.AB)
print("BC:", triangle.BC)
print("CA:", triangle.CA)
print("A:", triangle.A)
print("B:", triangle.B)
print("C:", triangle.C)

triangle.modify_angle('AB', 30)
triangle.modify_side('A', 1)

print("\nModified angles and sides:")
print("AB:", triangle.AB)
print("BC:", triangle.BC)
print("CA:", triangle.CA)
print("A:", triangle.A)
print("B:", triangle.B)
print("C:", triangle.C)

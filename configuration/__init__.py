from configuration.MotorConfiguration import motor


def configuration_for_vertical(vertical):
    if vertical == 'motor':
        return motor()

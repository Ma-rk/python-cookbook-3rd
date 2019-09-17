def recv(maxsize, *, block):
    print(f'Receives a message: maxsize={maxsize}, block={block}')


# recv(1024, True)  # TypeError
recv(1024, block=True)  # Ok

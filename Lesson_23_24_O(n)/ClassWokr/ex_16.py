import sys


class ValidationError(Exception):

   def __init__(self, *args, idx=None):
       self.idx = idx
       super().__init__(*args)


class StringValidator:

   def __init__(self):
       self._text = None
       self._opens = "([{<"
       self._closes = ")]}>"
       self._message = ''

   def _is_balanced(self):
       stack = []
       errors = []
       for symbol_position, symbol in enumerate(self._text):
           if symbol in self._opens:
               stack.append((symbol_position, symbol))  # [(1, '(')]
           elif symbol in self._closes:
               position = self._closes.index(symbol)
               if stack and (self._opens[position] == stack[-1][1]):
                   stack.pop()
               else:
                   errors.append(symbol_position)
       if errors or stack:
           errors.extend([s[0] for s in stack])
           self._get_message('Unbalanced brackets', sorted(errors))
           raise ValidationError(self._message, idx=sorted(errors))

   def _is_alphanumeric(self):
       allowed_symbols = f'{self._opens}{self._closes}_/ '
       errors = []
       for idx, symbol in enumerate(self._text):
           if symbol not in allowed_symbols and not symbol.isalnum():
               errors.append(idx)
       if errors:
           self._get_message('Wrong symbol(s)', errors)
           raise ValidationError(self._message, idx=sorted(errors))

   def _get_message(self, base: str, error_details: list):
       res = (', '.join(f"at {error}" for error in error_details))
       self._message = f"{base}: {res}"

   def _mark_errors(self, indexes):
       marks = ['^' if i in indexes else ' ' for i in range(len(self._text))]
       return f"{self._text}\n{''.join(marks)}"

   def validate(self, text):
       self._text = text
       try:
           self._is_alphanumeric(),
           self._is_balanced()
       except ValidationError as err:
           print(self._mark_errors(err.idx), file=sys.stderr)
           raise err
       return True


if __name__ == '__main__':
   input_text = '}<div><p>{ test }}</p</div>'
   validator = StringValidator()
   if validator.validate(input_text):
       print(input_text)
from lambda_function import lambda_handler
import unittest
import io
import sys
import json

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_handler(self):

        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # 准备测试输入
        test_input = json.dumps({"a": "aaaa", "b": "bbbb", "c": "cccc"})
        
        # 调用 lambda_handler
        lambda_handler(None, None)
        lambda_handler(test_input, None)
        
        # 恢复标准输出
        sys.stdout = sys.__stdout__
        
        # 检查输出
        output = captured_output.getvalue()
        self.assertIn("Done x1.1", output)

if __name__ == '__main__':
    unittest.main()
    
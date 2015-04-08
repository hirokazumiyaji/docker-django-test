from django.test import TestCase
import redis


class Test(TestCase):

  def setUp(self):
      self.r = redis.StrictRedis(host="redis")
      self.r.flushdb()

  def test_ok(self):
      self.assertEqual(1, 1)

  def test_error(self):
      self.assertEqual(2, 1)

  def test_redis(self):
      self.assertEqual(self.r.get("name"), None)

      self.r.set("name", "name")
      self.assertEqual(self.r.get("name"), "name")

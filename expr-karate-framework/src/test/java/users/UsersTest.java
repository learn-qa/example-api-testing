package users;

import com.intuit.karate.junit5.Karate;
import com.intuit.karate.junit5.Karate.Test;

public class UsersTest {
  @Test
  Karate testAll() {
    return Karate.run().relativeTo(getClass());
  }
}

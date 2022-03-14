package com.rocketscience.onlinecv;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class User {
  private String phone;
  private String email;
  private String address;
  private String lastName;
  private String firstName;
}
